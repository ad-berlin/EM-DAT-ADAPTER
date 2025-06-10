import streamlit as st
import plotly.express as px

from utils.variables import (YEAR_START, MONTH_START, DAY_START, YEAR_END, MONTH_END, DAY_END, COUNTRY, REGION,
                             SUBREGION, LOCATION, RIVER, NUM, DIS_NAT_TECH, DIS_SUBGROUP, DIS_TYPE, DIS_SUBTYPE, ORIGIN,
                             ASS_TYPES, AID, RECONSTRUCTION, RECONSTRUCTION_ADJ, INSURED, INSURED_ADJ, DAMAGE,
                             DAMAGE_ADJ, MAG, MAG_SCALE, DEATHS, INJURED, AFFECTED, HOMELESS, DATE_START, DATE_END,
                             DIS_DURATION,)
from utils.variables import bar_list, plot_list, money_list, info_list
from text.text_info import info_dict, error_dict, select_dict, emoji_dict, TEXT_IMPRESSUM
from utils.utils import write_help

if 'data' not in st.session_state:
    st.error(error_dict.get('ERROR_DATA'))

else:
    if 'dis_type_scope' not in st.session_state:
        st.session_state.dis_type_scope = DIS_SUBTYPE

    target = st.session_state['dis_type_scope']

    st.header(f":violet[Explore {target}s all over the world!]", divider="rainbow")
    df = st.session_state['data'].copy()

    latest_year = df[YEAR_START].max()
    earliest_year = df[YEAR_START].min()
    all_years = df[YEAR_START].unique()

    write_help('DIS_TYPE')

    with st.container(border=True):
        st.write(select_dict.get('SELECT_DIS_SCOPE'))
        st.radio(
            label="decision dis_type scope",
            options=[DIS_NAT_TECH, DIS_SUBGROUP, DIS_TYPE, DIS_SUBTYPE],
            label_visibility="collapsed",
            horizontal=True,
            key="dis_type_scope")

        st.write(select_dict.get('SELECT_TIME'))
        start, end = st.select_slider(label="timespan_dis_type",
                                      options=all_years,
                                      value=(earliest_year, latest_year),
                                      label_visibility="collapsed")
        df = df.loc[df[YEAR_START] >= start]
        df = df.loc[df[YEAR_START] <= end]

    st.subheader(f":blue[Overview per {target}s]", divider="green")
    df_target_count = df[target].value_counts()
    target_bar = px.bar(
        df_target_count,
        x=df_target_count.index,
        y='count',
        title=f"Number of Events Worldwide per {target}s")
    st.plotly_chart(target_bar)

    target_bar = px.scatter(
        df,
        x=DATE_START,
        y=DEATHS,
        color=target,
        hover_data=[COUNTRY, NUM],
        title=f"{DEATHS} Worldwide per {target}s")
    st.plotly_chart(target_bar)

    st.subheader(f":blue[Find out more about certain {target}s]", divider="green")
    selected_subtargets = st.multiselect(label="Find out more about a certain Disaster Subtype...",
                                         options=sorted(df[target].unique()),
                                         label_visibility="collapsed")
    if len(selected_subtargets) > 0:
        tabs = st.tabs(selected_subtargets)

        for ix, dis_target in enumerate(selected_subtargets):
            with tabs[ix]:
                st.subheader(f"{emoji_dict.get('EMOJI_SUBHEADER')} {dis_target}", divider="grey")
                fig_death = px.bar(
                    data_frame=df.loc[df[target] == dis_target],
                    x=SUBREGION,
                    y=DEATHS,
                    title=f"{DEATHS} of {dis_target} per {SUBREGION}",
                    hover_data=[COUNTRY, YEAR_START, NUM]
                )
                st.plotly_chart(fig_death)

                st.write("Explore further parameters:")
                selected_parameter = st.multiselect(label="more parameters",
                                                    options=sorted(plot_list),
                                                    label_visibility="collapsed",
                                                    key=f"parameter box {dis_target}")
                for parameter in selected_parameter:
                    st.subheader(f"{parameter}")
                    st.write(f"{info_dict.get(parameter)}")
                    if parameter in bar_list:
                        fig_bar = px.bar(
                            data_frame=df.loc[df[target] == dis_target],
                            x=SUBREGION,
                            y=parameter,
                            title=f"{parameter} of {dis_target} per {SUBREGION}",
                            hover_data=[COUNTRY, YEAR_START, NUM]
                        )
                        st.plotly_chart(fig_bar)
                    if parameter in info_list:
                        info = df.loc[df[DIS_SUBTYPE] == dis_target][parameter].dropna().unique()
                        st.write(f'{', '.join(info)}')

st.divider()
st.write(TEXT_IMPRESSUM)
