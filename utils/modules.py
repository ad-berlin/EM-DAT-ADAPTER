import streamlit as st

from text.text_info import help_dict, TEXT_HELP

def write_help(page_in_capitals) -> None:
    with st.expander(TEXT_HELP, icon=':material/info:'):
        st.markdown(help_dict.get(f'HELP_{page_in_capitals}'))