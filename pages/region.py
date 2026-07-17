import streamlit as st
import numpy as np
import pandas as pd

from utils import constants as c
from utils import modules as m
from utils import ut as u
from text import text_info as t

# specific page constants
KEY_REGION_SPEC = 'region_specification'
KEY_SUBREGION_SPEC = 'subregion_specification'
KEY_COUNTRY_SPEC = 'country_specification'

LST_REGION = [c.CONTINENT_R, c.OPT_REGION]
LST_SUBREGION = [c.GEOGRAPH_SR, c.OPT_SUBREGION]
LST_COUNTRY = [c.SOVEREIGN_C, c.OPT_COUNTRY, c.ADMIN_C, c.UN_M49_C]

st.subheader(t.HEADER, divider="grey")

if 'data' not in st.session_state:
    st.error(t.ERROR_DATA)

else:
    if 'dis_region_scope' not in st.session_state:
        st.session_state['dis_region_scope'] = c.COUNTRY
    if KEY_REGION_SPEC not in st.session_state:
        st.session_state[KEY_REGION_SPEC] = c.CONTINENT_R
    if KEY_SUBREGION_SPEC not in st.session_state:
        st.session_state[KEY_SUBREGION_SPEC] = c.GEOGRAPH_SR
    if KEY_COUNTRY_SPEC not in st.session_state:
        st.session_state[KEY_COUNTRY_SPEC] = c.SOVEREIGN_C

    # specific page variables
    target = st.session_state['dis_region_scope']

    region_view = st.session_state[KEY_REGION_SPEC]
    subregion_view = st.session_state[KEY_SUBREGION_SPEC]
    country_view = st.session_state[KEY_COUNTRY_SPEC]

    df = st.session_state['data'].copy()

    m.write_help(page_in_capitals='REGION')

    with st.container(border=True):
        col1, col2 = st.columns(2)
        col1.write(f":blue[{t.SELECT_DIS_SCOPE}]")
        col1.radio(
            label="decision dis_type scope",
            options=[c.REGION, c.SUBREGION, c.COUNTRY],
            label_visibility="collapsed",
            horizontal=True,
            key="dis_region_scope")

        col2.write(f":blue[{t.SELECT_GROUPING}]")
        if target == c.REGION:
            spec = col2.radio(
                label="decision region",
                options=LST_REGION,
                label_visibility="collapsed",
                horizontal=True,
                key=KEY_REGION_SPEC)

        if target == c.SUBREGION:
            spec = col2.radio(
                label="decision subregion",
                options=LST_SUBREGION,
                label_visibility="collapsed",
                horizontal=True,
                key=KEY_SUBREGION_SPEC)

        if target == c.COUNTRY:
            spec = col2.radio(
                label="decision country",
                options=LST_COUNTRY,
                label_visibility="collapsed",
                horizontal=True,
                key=KEY_COUNTRY_SPEC)

        start, end = m.write_time(data=df)
        df = df.loc[df[c.YEAR_START] >= start]
        df = df.loc[df[c.YEAR_START] <= end]

    with st.container(border=True):
        m.write_overview(target=spec, data=df, start=start, end=end, hover_list=[c.DIS_TYPE, c.NUM])

    st.warning(t.WARNING)

    with st.container(border=True):
        if spec != c.OPT_COUNTRY:
            spec_plural = f"{spec}s"
        else:
            spec_plural = "EM-DAT Countries"

        st.write(f":blue[I want to find out more about certain {spec_plural}]")

        col1, col2 = st.columns([1,2])
        trigger_filter_deep = col1.toggle("Apply filter of classification", key="toggle_deep")

        if trigger_filter_deep:
            classification_scope_deep = col2.radio(
                label="class scope filter deep",
                options=[c.DIS_SUBGROUP, c.DIS_TYPE, c.DIS_SUBTYPE],
                label_visibility="collapsed",
                horizontal=True)

            spec = m.write_dig_deep(target=spec, data=df, start=start,
                                      end=end, filter=True, filter_cat=classification_scope_deep)
        else:
            spec = m.write_dig_deep(target=spec, data=df, start=start, end=end)

    st.warning(t.WARNING)

    with st.container(border=True):
        if spec != c.OPT_COUNTRY:
            spec_plural = f"{spec}s"
        else:
            spec_plural = "EM-DAT Countries"

        st.write(f":blue[I want to compare {spec_plural} per chosen parameter]")

        col1, col2 = st.columns([1, 2])
        trigger_filter_compare = col1.toggle("Apply filter of classification", key="toggl_compare")

        if trigger_filter_compare:
            classification_scope_compare = col2.radio(
                label="class scope filter compare",
                options=[c.DIS_SUBGROUP, c.DIS_TYPE, c.DIS_SUBTYPE],
                label_visibility="collapsed",
                horizontal=True)

            spec = m.write_compare(target=spec, data=df, start=start,
                                   end=end, filter=True, filter_cat=classification_scope_compare)

        else:
            spec = m.write_compare(target=spec, data=df, start=start, end=end, filter=False)


m.write_impressum()
