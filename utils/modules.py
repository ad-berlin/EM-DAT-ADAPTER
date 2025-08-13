import streamlit as st

from text import text_info as t


def write_help(page_in_capitals) -> None:
    with st.expander(t.TEXT_HELP, icon=':material/info:'):
        st.markdown(t.help_dict.get(f'HELP_{page_in_capitals}'))


def write_scope() -> None:
    st.write("test123")


def write_time() -> None:
    st.write("test123")


def write_grouping() -> None:
    st.write("test123")

