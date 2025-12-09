import pandas as pd
import streamlit as st

from utils import constants as c
from utils import modules as m
from utils import ut as u
from text import text_info as t
from utils.constants import regions_list

st.subheader(t.HEADER, divider="grey")

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
        df, info = m.build_filter(data=df)

        st.write(":blue[...see the table, ...]")
        st.dataframe(df, hide_index=True)

        download = st.button(":blue[...and save as ExcelFile.]", use_container_width=True)
        if download:
            with pd.ExcelWriter("DisTrack_filtered.xlsx") as writer:
                df.to_excel(writer, sheet_name="filtered_data", index=False)
                info.to_excel(writer, sheet_name="filter_info")

m.write_impressum()
