import pandas as pd
import streamlit as st

from utils import constants as c
from utils import modules as m
from utils import ut as u
from text import text_info as t

if 'data' not in st.session_state:
    st.error(t.ERROR_DATA)

else:
    df = st.session_state['data'].copy()

    m.write_help(page_in_capitals='TABLE')

    with st.container(border=True):
        st.write(f":blue[I have the {c.NUM} and want to see the full dataset]")
        dis_no = st.text_input(label=f"{c.NUM} input",
                               label_visibility="collapsed",
                               placeholder=f"Please type the {c.NUM}")
        if dis_no:
            st.dataframe(df.loc[df[c.NUM] == dis_no], hide_index=True)

    with st.container(border=True):
        st.write(":blue[I want to filter certain parameters, ...]")

        filter_params = st.multiselect(label="params for filter",
                                       options=sorted(df.columns),
                                       label_visibility="collapsed",
                                       placeholder="Choose parameters for filter options")
        for param in filter_params:
            st.write(f"Choose category to filter {param}")
            argument = st.selectbox(label=f"{param} to filter",
                                    options=df[param].unique(),
                                    label_visibility="collapsed")
            df = df.loc[df[param] == argument]
            # argument = st.text_input(label=f"{param} to filter",
            #                          label_visibility="collapsed",
            #                          placeholder="Please type what you look for")
            # df = df.loc[df[param].str.contains(argument)]  # works if array does not contain NaN

        st.write(":blue[...see the table, ...]")
        st.dataframe(df, hide_index=True)
        download = st.button(":blue[...and save as ExcelFile]", use_container_width=True)
        if download:
            df.to_excel(pd.ExcelWriter("DisTrack_file_filtered"), index=False)
            # TODO: add second sheet with filter descriptor

m.write_impressum()
