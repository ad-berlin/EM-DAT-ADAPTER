import streamlit as st
import numpy as np
import pandas as pd

from utils import constants as c
from utils import modules as m
from utils import ut as u
from text import text_info as t

# specific page constants TODO: add to constants
KEY_REGION_SPEC = 'region_specification'
KEY_SUBREGION_SPEC = 'subregion_specification'
KEY_COUNTRY_SPEC = 'country_specification'
OPT_COUNTRY = 'EM-DAT Country'

LST_REGION = [c.CONTINENT_R, c.REGION]
LST_SUBREGION = [c.GEOGRAPH_SR, c.SUBREGION]
LST_COUNTRY = [c.SOVEREIGN_C, OPT_COUNTRY, c.ADMIN_C, c.UN_M49_C]

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
            if spec is OPT_COUNTRY:
                spec = c.COUNTRY

        start, end = m.write_time(data=df)
        df = df.loc[df[c.YEAR_START] >= start]
        df = df.loc[df[c.YEAR_START] <= end]

    # with st.container(border=True):  # TODO: Correct Areas need to be added!
    #
    #     # FOR DEVELOPMENT: AREA ANALYSIS
    #     un_df = u.get_un_data(file="data/UN_DEMOGRAPH.csv")
    #     un_df = un_df.loc[un_df['LocID'] <= 900]
    #     add_un_area = "CountryArea[km²]"
    #     un_df[add_un_area] = (un_df["TPopulation1Jan"] / un_df["PopDensity"]) * 1000
    #
    #     m49_df = pd.read_excel("data/UNSD.xlsx")
    #     m49_df_dict = m49_df.set_index("Country/Area")
    #     m49_df_dict = m49_df_dict.to_dict()
    #
    #     un_ctr = sorted(un_df['LocID'].unique())
    #     admin_ctr = sorted(m49_df[c.M49_CODE_C].unique())
    #
    #     for country in un_ctr:
    #         if country not in admin_ctr and country != 900:
    #             st.write(country)
    #
    #     not_in_un_lst = []
    #     for country in admin_ctr:
    #         if country not in un_ctr:
    #             not_in_un_lst.append(country)
    #
    #     for num in not_in_un_lst:
    #         st.write(m49_df_dict.get("Country/Area").get(num, "ERROR"))
    #
    #     area_dict = {}
    #     for country in sorted(df[c.ADMIN_C].unique()):
    #         country_code = m49_df_dict.get(c.M49_CODE_C).get(country)
    #         area = un_df.loc[un_df["LocID"] == country_code][add_un_area].mean()
    #         area_dict.update({country: area})
    #     # st.write(area_dict)  # TODO: multiple area_dicts are needed
    #
    #     st.write(f'{target}, {spec}')
    #     if spec == OPT_COUNTRY:
    #         spec = c.COUNTRY
    #     if spec == c.UN_M49_C:
    #         spec = c.COUNTRY
    #         df = df.loc[df[c.ISO_A2] != np.nan]
    #
    #     info = pd.DataFrame(df[spec].value_counts())
    #     info["new_col_area"] = info.index.map(lambda x: area_dict.get(x))
    #     info["new_col_event_per_area"] = info["count"] / info["new_col_area"]
    #
    #     st.dataframe(data=info,
    #                  column_config={
    #                      spec: st.column_config.TextColumn(label=target, width="large"),
    #                      "count": st.column_config.NumberColumn(label="number of events"),
    #                      "new_col_area": st.column_config.NumberColumn(label="Area/Region in km²"),
    #                      "new_col_event_per_area": st.column_config.NumberColumn(label="Events per km²")},
    #                  use_container_width=True)

    with st.container(border=True):
        m.write_overview(target=spec, data=df, start=start, end=end, hover_list=[c.DIS_TYPE, c.NUM])

    with st.container(border=True):
        selected_subtargets = m.write_dig_deep(target=spec, data=df, start=start, end=end, filter=False)

    with st.container(border=True):
        m.write_compare(target=spec, data=df, start=start, end=end, filter=True)

m.write_impressum()
