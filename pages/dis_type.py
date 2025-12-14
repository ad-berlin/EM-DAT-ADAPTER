import streamlit as st

from utils import constants as c
from utils import modules as m
from text import text_info as t

st.subheader(t.HEADER, divider="grey")

if 'data' not in st.session_state:
    st.error(t.ERROR_DATA)

else:
    if 'dis_type_scope' not in st.session_state:
        st.session_state.dis_type_scope = c.DIS_SUBTYPE

    target = st.session_state['dis_type_scope']

    df = st.session_state['data'].copy()

    m.write_help(page_in_capitals='DIS_TYPE')

    with st.container(border=True):
        st.write(f":blue[{t.SELECT_DIS_SCOPE}]")
        st.radio(
            label="scope",
            options=[c.DIS_SUBGROUP, c.DIS_TYPE, c.DIS_SUBTYPE],
            label_visibility="collapsed",
            horizontal=True,
            key="dis_type_scope")

        start, end = m.write_time(data=df)
        df = df.loc[df[c.YEAR_START] >= start]
        df = df.loc[df[c.YEAR_START] <= end]

    with st.container(border=True):
        m.write_overview(target=target, data=df, start=start, end=end, hover_list=[c.NUM])

    with st.container(border=True):
        m.write_dig_deep(target=target, start=start, end=end, data=df)

    with st.container(border=True):
        m.write_compare(target=target, data=df, start=start, end=end)

m.write_impressum()
