"""A small query language for the free text filter.

Supported syntax
----------------
    rain                CONTAINS      substring of the whole cell
    "heavy rain"        CONTAINS      phrase, spaces preserved
    =rain               EXACT         a unit of the cell equals the term
    ="heavy rainfall"   EXACT         same, for multi word labels
    rain*               STARTS_WITH   a unit of the cell starts with the term
    *fall               ENDS_WITH     a unit of the cell ends with the term
    *rain*              CONTAINS      equivalent to plain `rain`
    a AND b   /   a b   AND           whitespace implies AND
    a OR b              OR
    NOT a               NOT
    ( ... )             grouping

Precedence: NOT > AND > OR. Everything is case and diacritic insensitive.

What a "unit" is
----------------
Every cell is broken into the whole normalised cell PLUS its parts. The
separator decides what a part is:

    sep = None   ->  parts are words          (Origin (clean), Location, ...)
    sep = "; "   ->  parts are labels         (Origin (label))

That is why EXACT means "the word rain" on Origin (clean) but "the label
heavy rainfall" on Origin (label). CONTAINS always works on the whole cell,
so that a quoted phrase spanning several words still matches.

Leaves are evaluated against every column in scope and OR-ed, i.e. a term
matches a row if it is found in any of the searched columns.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

import numpy as np
import pandas as pd
from unidecode import unidecode

# --- match modes -------------------------------------------------------------
CONTAINS = "CONTAINS"
EXACT = "EXACT"
STARTS_WITH = "STARTS_WITH"
ENDS_WITH = "ENDS_WITH"


class QueryError(ValueError):
    """Raised for a malformed query. Message is meant for the end user."""


# --- normalisation -----------------------------------------------------------
def normalise(value) -> str:
    """ascii, lower case, collapsed whitespace. Mirrors ut.treat_text_column."""
    text = unidecode(str(value)).lower().strip()
    return re.sub(r"\s+", " ", text)


def unitise(series: pd.Series, sep: str | None = None) -> pd.Series:
    """Break every cell into its comparable units: whole cell plus parts."""
    def _units(value):
        cell = normalise(value)
        if not cell:
            return []
        if sep:
            parts = [normalise(part) for part in str(value).split(sep)]
        else:
            parts = cell.split(" ")
        parts = [part for part in parts if part]
        return list(dict.fromkeys([cell] + parts))

    return series.fillna("").map(_units)


def prepare(data: pd.DataFrame, columns, seps: dict | None = None) -> dict:
    """Pre-compute the normalised cells and units for every column in scope.

    Returns {column: (cells, units)}. Done once per query rather than once per
    term, because a query with five terms would otherwise re-normalise the
    same column five times.
    """
    seps = seps or {}
    prepared = {}
    for column in columns:
        cells = data[column].fillna("").map(normalise)
        units = unitise(data[column], sep=seps.get(column))
        prepared[column] = (cells, units)
    return prepared


# --- abstract syntax tree ----------------------------------------------------
@dataclass
class Term:
    text: str
    mode: str = CONTAINS


@dataclass
class Not:
    child: object


@dataclass
class And:
    children: list = field(default_factory=list)


@dataclass
class Or:
    children: list = field(default_factory=list)


# --- tokeniser ---------------------------------------------------------------
# Order matters: the quoted alternatives must be tried before the bare word,
# otherwise ="heavy rain" would be cut at the blank.
_TOKEN_RE = re.compile(r'\(|\)|=?"[^"]*"|[^\s()"]+')

_KEYWORDS = {"AND": "AND", "OR": "OR", "NOT": "NOT", "&": "AND", "|": "OR"}


def _make_term(raw: str) -> Term:
    mode = CONTAINS

    if raw.startswith("="):
        mode = EXACT
        raw = raw[1:]

    if len(raw) >= 2 and raw.startswith('"') and raw.endswith('"'):
        return Term(normalise(raw[1:-1]), mode)

    if mode is CONTAINS and raw not in ("*", "**"):
        starts, ends = raw.endswith("*"), raw.startswith("*")
        if starts and ends:
            raw = raw[1:-1]
        elif starts:
            raw, mode = raw[:-1], STARTS_WITH
        elif ends:
            raw, mode = raw[1:], ENDS_WITH

    text = normalise(raw)
    if not text:
        raise QueryError("Empty search term.")
    return Term(text, mode)


def _tokenise_query(query: str) -> list:
    tokens = []
    for raw in _TOKEN_RE.findall(query):
        if raw == "(":
            tokens.append(("LPAREN", None))
        elif raw == ")":
            tokens.append(("RPAREN", None))
        elif raw.upper() in _KEYWORDS:
            tokens.append((_KEYWORDS[raw.upper()], None))
        else:
            tokens.append(("TERM", _make_term(raw)))
    return tokens


# --- parser (recursive descent, precedence NOT > AND > OR) -------------------
class _Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def _peek(self):
        return self.tokens[self.pos][0] if self.pos < len(self.tokens) else "EOF"

    def _next(self):
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def parse(self):
        node = self._parse_or()
        if self._peek() != "EOF":
            raise QueryError('Unbalanced ")" in the query.')
        return node

    def _parse_or(self):
        children = [self._parse_and()]
        while self._peek() == "OR":
            self._next()
            children.append(self._parse_and())
        return children[0] if len(children) == 1 else Or(children)

    def _parse_and(self):
        children = [self._parse_unary()]
        while self._peek() in ("AND", "NOT", "TERM", "LPAREN"):
            if self._peek() == "AND":
                self._next()
            children.append(self._parse_unary())
        return children[0] if len(children) == 1 else And(children)

    def _parse_unary(self):
        kind = self._peek()
        if kind == "NOT":
            self._next()
            return Not(self._parse_unary())
        if kind == "LPAREN":
            self._next()
            node = self._parse_or()
            if self._peek() != "RPAREN":
                raise QueryError('Missing ")" in the query.')
            self._next()
            return node
        if kind == "TERM":
            return self._next()[1]
        if kind == "EOF":
            raise QueryError("The query ends after an operator.")
        raise QueryError(f"Unexpected {kind} in the query.")


def parse(query: str):
    """Parse a query string into an AST. Empty query returns None."""
    tokens = _tokenise_query(query or "")
    if not tokens:
        return None
    return _Parser(tokens).parse()


# --- evaluation --------------------------------------------------------------
_UNIT_PREDICATES = {
    EXACT: lambda unit, term: unit == term,
    STARTS_WITH: lambda unit, term: unit.startswith(term),
    ENDS_WITH: lambda unit, term: unit.endswith(term),
}


def _term_mask(cells: pd.Series, units: pd.Series, term: Term) -> np.ndarray:
    if term.mode == CONTAINS:
        return cells.str.contains(term.text, regex=False, na=False).to_numpy()
    predicate = _UNIT_PREDICATES[term.mode]
    return units.map(lambda us: any(predicate(u, term.text) for u in us)).to_numpy()


def evaluate(node, prepared: dict, index) -> pd.Series:
    """Turn an AST into a boolean mask over the prepared columns."""
    if node is None:
        return pd.Series(True, index=index)

    if isinstance(node, Term):
        if not prepared:
            raise QueryError("No column selected to search in.")
        masks = [_term_mask(cells, units, node) for cells, units in prepared.values()]
        return pd.Series(np.logical_or.reduce(masks), index=index)

    if isinstance(node, Not):
        return ~evaluate(node.child, prepared, index)

    if isinstance(node, (And, Or)):
        reducer = np.logical_and if isinstance(node, And) else np.logical_or
        masks = [evaluate(child, prepared, index).to_numpy() for child in node.children]
        return pd.Series(reducer.reduce(masks), index=index)

    raise QueryError(f"Cannot evaluate {type(node).__name__}.")


def run(data: pd.DataFrame, query: str, columns, seps: dict | None = None) -> pd.Series:
    """Parse and evaluate in one step. Returns a boolean mask."""
    node = parse(query)
    if node is None:
        return pd.Series(True, index=data.index)
    prepared = prepare(data, columns, seps)
    return evaluate(node, prepared, data.index)


# --- rendering ---------------------------------------------------------------
_SYMBOLS = {CONTAINS: "~", EXACT: "=", STARTS_WITH: "^", ENDS_WITH: "$"}


def to_string(node) -> str:
    """Render an AST back into a canonical expression for the info table."""
    if node is None:
        return "-"
    if isinstance(node, Term):
        return f'{_SYMBOLS[node.mode]}"{node.text}"'
    if isinstance(node, Not):
        return f"NOT {to_string(node.child)}"
    if isinstance(node, And):
        return "(" + " AND ".join(to_string(ch) for ch in node.children) + ")"
    if isinstance(node, Or):
        return "(" + " OR ".join(to_string(ch) for ch in node.children) + ")"
    return str(node)
