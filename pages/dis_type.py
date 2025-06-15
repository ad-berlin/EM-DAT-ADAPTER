import streamlit as st
import plotly.express as px
import numpy as np

from utils.variables import (YEAR_START, MONTH_START, DAY_START, YEAR_END, MONTH_END, DAY_END, COUNTRY, REGION,
                             SUBREGION, LOCATION, RIVER, NUM, DIS_NAT_TECH, DIS_SUBGROUP, DIS_TYPE, DIS_SUBTYPE, ORIGIN,
                             ASS_TYPES, AID, RECONSTRUCTION, RECONSTRUCTION_ADJ, INSURED, INSURED_ADJ, DAMAGE,
                             DAMAGE_ADJ, MAG, MAG_SCALE, DEATHS, INJURED, AFFECTED, HOMELESS, DATE_START, DATE_END,
                             DIS_DURATION, )
from utils.variables import bar_list, plot_list, money_list, info_list
from text.text_info import info_dict, error_dict, select_dict, emoji_dict, TEXT_IMPRESSUM
from utils.utils import write_help

if 'data' not in st.session_state:
    st.error(error_dict.get('ERROR_DATA'))

else:
    if 'dis_type_scope' not in st.session_state:
        st.session_state.dis_type_scope = DIS_SUBTYPE

    target = st.session_state['dis_type_scope']

    st.header(f":violet[Explore {target}s all over the World!]", divider="rainbow")
    df = st.session_state['data'].copy()

    latest_year = df[YEAR_START].max()
    earliest_year = df[YEAR_START].min()
    all_years = df[YEAR_START].unique()

    write_help(page_in_capitals='DIS_TYPE')

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

    target_scatter = px.scatter(
        df,
        x=DATE_START,
        y=DEATHS,
        color=target,
        hover_data=[COUNTRY, NUM],
        title=f"{DEATHS} Worldwide per {target}s")
    st.plotly_chart(target_scatter)

    st.subheader(f":blue[Find out more about certain {target}s]", divider="green")
    selected_subtargets = st.multiselect(label="Find out more about a certain Disaster Subtype...",
                                         options=sorted(df[target].unique()),
                                         label_visibility="collapsed")
    if len(selected_subtargets) > 0:
        tabs = st.tabs(selected_subtargets)

        for ix, dis_target in enumerate(selected_subtargets):
            with tabs[ix]:
                st.subheader(f"{emoji_dict.get('EMOJI_SUBHEADER')} {dis_target}", divider="grey")
                target_df = df.loc[df[target] == dis_target]

                fig_death = px.bar(
                    data_frame=target_df,
                    x=SUBREGION,
                    y=DEATHS,
                    title=f"{DEATHS} of {dis_target} per {SUBREGION}",
                    subtitle="with number of events provided",
                    hover_data=[COUNTRY, YEAR_START, NUM])

                # TODO: Fix difference between plotly and manual aggregation
                event_count = target_df[SUBREGION].value_counts()
                death_count = target_df.groupby(SUBREGION)[DEATHS].sum()

                for cat in target_df[SUBREGION].unique():
                    fig_death.add_annotation(
                        x=cat,
                        y=int(death_count.max()),
                        yshift=10,
                        text=str(event_count.get(cat, 0)),
                        showarrow=False,
                        font=dict(size=12, color="grey"),
                    )
                fig_death.update_layout()
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

    st.subheader(f":blue[Compare {target}s in impact per chosen parameter]", divider="green")
    request_subgroups = st.multiselect(label="subgroup for box comparison",
                                       options=df[target].unique(),
                                       label_visibility="collapsed",
                                       key=f"subgroup select")

    request_parameter = st.selectbox(label="parameters for box comparison",
                                     options=sorted(bar_list),
                                     label_visibility="collapsed",
                                     key=f"parameter select")

    if len(request_subgroups) > 0:
        df["request"] = np.where(df[target].isin(request_subgroups), 'request', 'no')
        df_request = df.loc[df[f"request"] == "request"]
        event_count = df_request[target].value_counts()

        box, table = st.tabs(['Plot', 'Table'])

        with box:
            fig_box = px.box(
                data_frame=df_request,
                x=target,
                y=request_parameter,
                title=f"{request_parameter} per selected {target}s",
                hover_data=[YEAR_START, COUNTRY, NUM])

            for cat in request_subgroups:
                fig_box.add_annotation(
                    x=cat,
                    y=df_request[request_parameter].max(),
                    yshift=10,
                    text=f'{str(event_count.get(cat, 0))} events',
                    showarrow=False,
                    font=dict(size=12, color="grey"),
                )
            fig_box.update_layout()
            st.write("")
            st.plotly_chart(fig_box)

        with table:
            st.write("A table will follow!")

st.divider()
st.write(TEXT_IMPRESSUM)

# TODO: remember
# death_count_1 = target_df.groupby(SUBREGION).agg({DEATHS : ['sum']})
