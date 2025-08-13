import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd

from utils import constants as c
from utils import modules as m
from utils import ut as u
from text import text_info as t

# specific page constants todo: add to constants
KEY_REGION_SPEC = 'region_specification'
KEY_SUBREGION_SPEC = 'subregion_specification'
KEY_COUNTRY_SPEC = 'country_specification'

OPT_COUNTRY = 'EM-DAT Countries'

LST_REGION = [c.CONTINENT, c.UN_M49_R]
LST_SUBREGION = [c.GEOGRAPH_R, c.UN_M49_SUBR]
LST_COUNTRY = [c.SOVEREIGN_C, OPT_COUNTRY, c.ADMIN_C, c.UN_M49_C]

if 'data' not in st.session_state:
    st.error(t.ERROR_DATA)

else:
    if 'dis_region_scope' not in st.session_state:
        st.session_state['dis_region_scope'] = c.COUNTRY
    if KEY_REGION_SPEC not in st.session_state:
        st.session_state[KEY_REGION_SPEC] = c.CONTINENT
    if KEY_SUBREGION_SPEC not in st.session_state:
        st.session_state[KEY_SUBREGION_SPEC] = c.GEOGRAPH_R
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
        col1.write(t.SELECT_DIS_SCOPE)
        col1.radio(
            label="decision dis_type scope",
            options=[c.REGION, c.SUBREGION, c.COUNTRY],
            label_visibility="collapsed",
            horizontal=True,
            key="dis_region_scope")

        col2.write(t.SELECT_GROUPING)
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
        ### For development!
        st.write(f'{target}, {spec}')
        st.write(df[target].unique())
        st.write(df[spec].unique())
        info = df[target].value_counts()
        st.dataframe(data=info,
                     column_config={
                         target: st.column_config.TextColumn(label=target, width="large"),
                         "count": st.column_config.NumberColumn(label="number of events")},
                     use_container_width=True)

    with st.container(border=True):
        m.write_overview(target=target, data=df, start=start, end=end, hover_list=[c.DIS_TYPE, c.NUM])

    with st.container(border=True):
        selected_subtargets = m.write_dig_deep(target=target, data=df, start=start, end=end)

        if 'un_data' in st.session_state:  # TODO: properly merge for insight!
            un_df = st.session_state['un_data'].copy()
            un_df = un_df.loc[un_df['Time'] >= start]
            un_df = un_df.loc[un_df['Time'] <= end]
            info = un_df.loc[un_df['Location'].str.contains(selected_subtargets)]
            st.dataframe(info)

    with st.container(border=True):
        m.write_compare(target=target, data=df, start=start, end=end)  # TODO: doesn't really make sense yet...

m.write_impressum()

