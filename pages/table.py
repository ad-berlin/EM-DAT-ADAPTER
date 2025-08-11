import streamlit as st

from utils import constants as c
from utils import modules as m
from text.text_info import TEXT_IMPRESSUM, error_dict, select_dict, month_dict
from utils.ut import treat_text_column, build_scatter_data

if 'data' not in st.session_state:
    st.error(error_dict.get('ERROR_DATA'))

else:
    df = st.session_state['data'].copy()

    m.write_help(page_in_capitals='TABLE')

    with st.container(border=True):
        st.write(f":blue[I have the {c.NUM} and want to see the full dataset...]")
        dis_no = st.text_input(label=f"{c.NUM} input",
                               label_visibility="collapsed",
                               placeholder=f"Please type the {c.NUM}")
        if dis_no:
            st.dataframe(df.loc[df[c.NUM] == dis_no], hide_index=True)

    with st.container(border=True):
        st.write(":blue[I want to filter certain parameters...]")

        st.write(f"{select_dict.get('SELECT_PARAM')} for filter options")
        filter_params = st.multiselect(label="params for filter",
                                       options=sorted(df.columns),
                                       label_visibility="collapsed")
        for param in filter_params:
            st.write(f"Choose category to filter {param}")
            argument = st.selectbox(label=f"{param} to filter",
                                      options=sorted(df[param].unique()),
                                      label_visibility="collapsed")
            df = df.loc[df[param] == argument]

        st.write(":blue[...and see the table.]")
        st.dataframe(df, hide_index=True)

st.divider()
st.write(TEXT_IMPRESSUM)
