"""Filter section for utils/modules.py — complete and consistent.

Requires in utils/constants.py
------------------------------
    # LAT/LONG must NOT live in int_list: build_scatter_data() fills every
    # int_list column with 0, which would park coordinate-less events at 0/0.
    int_list = [
        INJURED, AFFECTED, HOMELESS, DEATHS, TOT_AFFECTED, RECONSTRUCTION,
        RECONSTRUCTION_ADJ, INSURED, INSURED_ADJ, DAMAGE, DAMAGE_ADJ,
        DIS_DURATION, MAG,
    ]

    # continuous columns: range slider in the filter, never fillna(0)
    float_list = [LAT, LONG]

    query_sep = {
        ORIGIN: None,
        ORIGIN_CLEAN: None,
        ORIGIN_LABEL: "; ",
        LOCATION: None,
        RIVER: None,
        ASS_TYPES: None,
        NAME: None,
        EXT_ID: "|",
    }
    query_list = list(query_sep)

    # only small, controlled vocabularies belong here
    multi_value_sep = {
        ORIGIN_LABEL: "; ",
    }

Which widget a column gets
-------------------------
    int_list / date_list / float_list  -> slider only
    multi_value_sep                    -> token multiselect + query field
    query_list (not multi value)       -> query field only
    everything else                    -> multiselect only
"""

import pandas as pd
import streamlit as st

from utils import constants as c
from utils import query as q
from text import text_info as t


def write_query(data, scope):
    """Free text query on a single column. Returns (mask, entry) or (None, None)."""
    query = st.text_input(
        label=f"{scope} query",
        placeholder="e.g.  (heavy OR torrential) AND rain* NOT snow",
        label_visibility="collapsed",
        key=f"query_{scope}")

    if not query.strip():
        return None, None

    try:
        node = q.parse(query)
        # scope is a single column name: it has to be wrapped, otherwise
        # q.prepare() iterates over the letters of the string.
        prepared = q.prepare(data, columns=[scope], seps=c.query_sep)
        mask = q.evaluate(node, prepared, data.index)
    except q.QueryError as error:
        st.error(f"{error} Check the query syntax in the help above.")
        return None, None

    st.caption(f"{int(mask.sum()):,} of {len(data):,} events match "
               f"`{q.to_string(node)}`")

    return mask, (scope, q.to_string(node))


def _token_clause(data, param, sep):
    """Multiselect over the parts of a multi value column, joined by AND or OR."""
    col_terms, col_comb = st.columns([5, 1])

    options = data[param].dropna().astype(str)
    options = pd.Series(sep.join(options).split(sep)).str.strip()
    options = sorted(options[options != ""].unique())

    terms = col_terms.multiselect(
        label=f"{param} to filter",
        options=options,
        placeholder=f"Choose {param}",
        label_visibility="collapsed",
        key=f"terms_{param}")

    combinator = col_comb.radio(
        label=f"{param} combinator",
        options=("OR", "AND"),
        horizontal=True,
        label_visibility="collapsed",
        key=f"comb_{param}",
        disabled=len(terms) < 2)

    if not terms:
        return None, None

    # Build the AST directly instead of composing a query string and parsing it
    # back: a label containing a quote would otherwise break its own query.
    leaves = [q.Term(q.normalise(term), q.EXACT) for term in terms]
    if len(leaves) == 1:
        node = leaves[0]
    else:
        node = q.And(leaves) if combinator == "AND" else q.Or(leaves)

    prepared = q.prepare(data, columns=[param], seps=c.query_sep)
    mask = q.evaluate(node, prepared, data.index)
    return mask, (param, q.to_string(node))


def _range_clause(data, param):
    """Slider for numeric and date columns."""
    col_slider, col_flags = st.columns([4, 1])

    values = data[param].dropna()
    if values.empty:
        st.error(t.ERROR_VALUE)
        return None, None

    if param in c.float_list:
        # Continuous: a select_slider would offer thousands of single floats.
        low, high = float(values.min()), float(values.max())
        min_val, max_val = col_slider.slider(
            label=f"{param} to filter",
            min_value=low,
            max_value=high,
            value=(low, high),
            label_visibility="collapsed",
            key=f"range_{param}")
    else:
        options = sorted(values.unique())
        min_val, max_val = col_slider.select_slider(
            label=f"{param} to filter",
            options=options,
            value=(options[0], options[-1]),
            label_visibility="collapsed",
            key=f"range_{param}")

    keep_na = col_flags.toggle("show nan values", key=f"na_{param}")

    mask = data[param].between(min_val, max_val)
    description = f"{min_val} to {max_val}"
    if keep_na:
        mask = mask | data[param].isna()
        description = f"{description}, incl. nan"

    return mask, (param, description)


def _category_clause(data, param):
    """Plain multiselect for single value columns."""
    argument = st.multiselect(
        label=f"{param} to filter",
        options=sorted(data[param].dropna().astype(str).unique()),
        placeholder=f"Choose {param}",
        label_visibility="collapsed",
        key=f"terms_{param}")

    if not argument:
        return None, None

    mask = data[param].astype(str).isin(argument)
    return mask, (param, ", ".join(argument))


def _clauses(data, param):
    """Render every widget that applies to one column and return their clauses.

    A column may contribute more than one clause. Returning a list rather than a
    single mask is what lets the branches coexist: nothing overwrites anything,
    and nothing is appended twice.
    """
    clauses = []

    if param in c.int_list or param in c.date_list or param in c.float_list:
        clauses.append(_range_clause(data, param))

    elif param in c.multi_value_sep:
        clauses.append(_token_clause(data, param, sep=c.multi_value_sep[param]))

    elif param not in c.query_list:
        clauses.append(_category_clause(data, param))

    # additive, not exclusive: runs on top of the token multiselect above
    if param in c.query_list:
        clauses.append(write_query(data=data, scope=param))

    return clauses


def build_filter(data):
    """Filter UI. Returns (filtered_data, info_table).

    Every widget contributes a boolean mask over the untouched frame; the masks
    are AND-ed at the very end. That keeps every option list derived from the
    same data, so the order in which columns are picked no longer changes what
    is selectable.
    """
    help_slot = st.container()

    masks = []
    info = []

    filter_params = st.multiselect(
        label="params for filter",
        options=sorted(c.filter_list),
        label_visibility="collapsed",
        placeholder="Choose parameters for filter options")

    # The help only appears once a column that understands the syntax is picked.
    if any(param in c.query_list for param in filter_params):
        with help_slot.expander("Query Syntax", icon=":material/help:"):
            st.markdown(t.QUERY_HELP)

    for param in filter_params:
        st.write(f"Filter :blue[{param}]")

        for mask, entry in _clauses(data, param):
            if mask is not None:
                masks.append(mask)
                info.append(entry)

    if masks:
        combined = masks[0]
        for mask in masks[1:]:
            combined = combined & mask
        data = data.loc[combined]

    info = pd.DataFrame(info, columns=["parameter", "query"])
    return data, info
