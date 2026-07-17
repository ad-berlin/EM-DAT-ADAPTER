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

    st.warning(t.WARNING)

    with st.container(border=True):
        target_plural = f"{target}s"
        st.write(f":blue[I want to find out more about certain {target_plural}]")

        col1, col2 = st.columns([1,2])
        trigger_filter_deep = col1.toggle("Apply filter of region", key="toggle_deep")

        if trigger_filter_deep:
            classification_scope_deep = col2.radio(
                label="class scope filter deep",
                options=[c.OPT_REGION, c.OPT_SUBREGION, c.UN_M49_C],
                label_visibility="collapsed",
                horizontal=True)
            target = m.write_dig_deep(target=target, start=start, end=end,
                             data=df, filter=True, filter_cat=classification_scope_deep)

        else:
            target = m.write_dig_deep(target=target, start=start, end=end, data=df)

    st.warning(t.WARNING)

    with st.container(border=True):
        target_plural = f"{target}s"
        st.write(f":blue[I want to compare {target_plural} per chosen parameter]")

        col1, col2 = st.columns([1, 2])
        trigger_filter_compare = col1.toggle("Apply filter of region", key="toggl_compare")

        if trigger_filter_compare:
            classification_scope_compare = col2.radio(
                label="class scope filter compare",
                options=[c.OPT_REGION, c.OPT_SUBREGION, c.UN_M49_C],
                label_visibility="collapsed",
                horizontal=True)

            spec = m.write_compare(target=target, data=df, start=start,
                                   end=end, filter=True, filter_cat=classification_scope_compare)

        else:
            spec = m.write_compare(target=target, data=df, start=start, end=end, filter=False)


m.write_impressum()
