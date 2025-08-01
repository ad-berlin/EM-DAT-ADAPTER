import streamlit as st
import plotly.express as px
import numpy as np

from utils import constants as c

from text.text_info import (info_dict, error_dict, select_dict, emoji_dict, TEXT_IMPRESSUM,)
from text.countries import (country_local_name_un_2025_dict, country_label_dict, non_self_gov_2025_dict,
                            overseas_terr_dict, non_un_2025_states)
from utils.ut import write_help, treat_text_column

# specific page constants todo: add to constants
KEY_REGION_SPEC = 'region_specification'
KEY_SUBREGION_SPEC = 'subregion_specification'
KEY_COUNTRY_SPEC = 'country_specification'
OPT_CONTINENT = 'Continents'
OPT_UN_M49_R = 'UN M49 Regions'
OPT_GEOGRAPH = 'Geographical Regions'
OPT_UN_M49_SUBR = 'UN M49 Subregions'
OPT_SOVEREIGN = 'UN Sovereign Countries'
OPT_COUNTRY = 'EM-DAT Countries'
OPT_ADMIN = 'Administrative Regions'
OPT_M49_C = 'UN M49 Countries'
LST_REGION = [OPT_CONTINENT, OPT_UN_M49_R]
LST_SUBREGION = [OPT_GEOGRAPH, OPT_UN_M49_SUBR]
LST_COUNTRY = [OPT_SOVEREIGN, OPT_COUNTRY, OPT_ADMIN, OPT_M49_C]


if 'data' not in st.session_state:
    st.error(error_dict.get('ERROR_DATA'))

else:
    if 'dis_region_scope' not in st.session_state:
        st.session_state['dis_region_scope'] = c.COUNTRY
    if KEY_REGION_SPEC not in st.session_state:
        st.session_state[KEY_REGION_SPEC] = OPT_CONTINENT
    if KEY_SUBREGION_SPEC not in st.session_state:
        st.session_state[KEY_SUBREGION_SPEC] = OPT_GEOGRAPH
    if KEY_COUNTRY_SPEC not in st.session_state:
        st.session_state[KEY_COUNTRY_SPEC] = OPT_SOVEREIGN

    # specific page variables
    target = st.session_state['dis_region_scope']
    region_view = st.session_state[KEY_REGION_SPEC]
    subregion_view = st.session_state[KEY_SUBREGION_SPEC]
    country_view = st.session_state[KEY_COUNTRY_SPEC]

    df = st.session_state['data'].copy()

    latest_year = df[c.YEAR_START].max()
    earliest_year = df[c.YEAR_START].min()
    all_years = sorted(df[c.YEAR_START].unique())

    # start actual content
    st.header(f":violet[Explore Disasters all over the World per {target}!]", divider="rainbow")
    write_help(page_in_capitals='REGION')

    with st.container(border=True):
        col1, col2 = st.columns(2)
        col1.write(select_dict.get('SELECT_DIS_SCOPE'))
        col1.radio(
            label="decision dis_type scope",
            options=[c.REGION, c.SUBREGION, c.COUNTRY],
            label_visibility="collapsed",
            horizontal=True,
            key="dis_region_scope")

        col2.write(select_dict.get('SELECT_GROUPING'))
        if target == c.REGION:
            col2.radio(
            label="decision region",
            options=LST_REGION,
            label_visibility="collapsed",
            horizontal=True,
            key=KEY_REGION_SPEC)

        if target == c.SUBREGION:
            col2.radio(
            label="decision subregion",
            options=LST_SUBREGION,
            label_visibility="collapsed",
            horizontal=True,
            key=KEY_SUBREGION_SPEC)

        if target == c.COUNTRY:
            col2.radio(
            label="decision country",
            options=LST_COUNTRY,
            label_visibility="collapsed",
            horizontal=True,
            key=KEY_COUNTRY_SPEC)

        st.write(select_dict.get('SELECT_TIME'))
        start, end = st.select_slider(label="timespan_region",
                                      options=sorted(all_years),
                                      value=(earliest_year, latest_year),
                                      label_visibility="collapsed")
        df = df.loc[df[c.YEAR_START] >= start]
        df = df.loc[df[c.YEAR_START] <= end]

    st.subheader(f":blue[Overview per {target}]", divider="green")

    # TODO: link to radio
    # df.replace({target: country_label_dict}, inplace=True)
    # df.replace({target: non_self_gov_2025_dict}, inplace=True)
    # df.replace({target: overseas_terr_dict}, inplace=True)
    # df.replace({target: non_un_2025_states}, inplace=True)
    # df.replace({target: country_local_name_un_2025_dict}, inplace=True)

    st.write(df[c.COUNTRY].unique())

    info = df[target].value_counts()
    st.dataframe(data=info,
                 column_config={
                     target: st.column_config.TextColumn(label=target, width="large"),
                     "count": st.column_config.NumberColumn(label="number of events")},
                 use_container_width=True)

    target_scatter = px.scatter(
        df,
        x=c.DATE_START,
        y=c.DEATHS,
        color=target,
        hover_data=[c.COUNTRY, c.DIS_TYPE, c.NUM],
        title=f"{c.DEATHS} Worldwide per {target} ({start} to {end})")
    st.plotly_chart(target_scatter)

    st.write(select_dict.get(f'SELECT_{target.upper()}'))
    disaster_region = st.selectbox(label="specific_dis_region",
                                   options=sorted(df[target].unique()),
                                   label_visibility="collapsed")
    df = df.loc[df[target] == disaster_region]


    # col3.write("📍 Focus Regions:")
    # keyword_1 = col3.text_input(label="Focus Region 1",
    #                             label_visibility="collapsed",
    #                             placeholder="please enter location")
    # keyword_2 = col3.text_input(label="Focus Region 2",
    #                             label_visibility="collapsed",
    #                             placeholder="please enter location")
    # keyword_3 = col3.text_input(label="Focus Region 3",
    #                             label_visibility="collapsed",
    #                             placeholder="please enter location")
    # KEYWORDS = [keyword_1, keyword_2, keyword_3]
    # keyword_pattern = '|'.join(KEYWORDS)
    # add_col_wanted_region = "Part of Research Region"
    # df_tab2[add_col_wanted_region] = np.where(df_tab2[LOCATION].str.contains(keyword_pattern, na=False), 'yes', 'no')
    # df_tab2 = df_tab2.loc[df_tab2[add_col_wanted_region] == "yes"]

    st.subheader(f":blue[{c.DEATHS} in {disaster_region} per Time]", divider="green")

    # plot deaths general
    history_of_death = px.scatter(
        data_frame=df,
        x=c.DATE_START,
        y=c.DEATHS,
        color=c.DIS_SUBGROUP,
        hover_data=[c.DIS_TYPE, c.DIS_SUBTYPE, c.DIS_DURATION, c.NUM],
        title=f"{c.DEATHS} (if no number available = 0) per {c.DIS_SUBGROUP} ({start} to {end})")
    history_of_death.update_traces(marker_size=10)
    st.plotly_chart(history_of_death)


    if 'un_data' in st.session_state:
        un_df = st.session_state['un_data'].copy()
        un_df = un_df.loc[un_df['Time'] >= start]
        un_df = un_df.loc[un_df['Time'] <= end]
        info = un_df.loc[un_df['Location'].str.contains(disaster_region)]  # TODO: fix weird categories
        st.dataframe(info)

st.divider()
st.write(TEXT_IMPRESSUM)