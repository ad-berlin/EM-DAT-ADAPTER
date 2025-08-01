import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd

from utils import constants as c
from text.text_info import info_dict, error_dict, select_dict, emoji_dict, TEXT_IMPRESSUM, help_dict, month_dict
from utils.ut import write_help, treat_text_column


if 'data' not in st.session_state:
    st.error(error_dict.get('ERROR_DATA'))

else:
    if 'dis_type_scope' not in st.session_state:
        st.session_state.dis_type_scope = c.DIS_SUBTYPE

    target = st.session_state['dis_type_scope']

    st.header(f":violet[Explore {target}s all over the World!]", divider="rainbow")
    df = st.session_state['data'].copy()

    latest_year = df[c.YEAR_START].max()
    earliest_year = df[c.YEAR_START].min()
    all_years = df[c.YEAR_START].unique()

    write_help(page_in_capitals='DIS_TYPE')

    with st.container(border=True):
        st.write(select_dict.get('SELECT_DIS_SCOPE'))
        st.radio(
            label="decision dis_type scope",
            options=[c.DIS_SUBGROUP, c.DIS_TYPE, c.DIS_SUBTYPE],
            label_visibility="collapsed",
            horizontal=True,
            key="dis_type_scope")

        st.write(select_dict.get('SELECT_TIME'))
        start, end = st.select_slider(label="timespan_dis_type",
                                      options=all_years,
                                      value=(earliest_year, latest_year),
                                      label_visibility="collapsed")
        df = df.loc[df[c.YEAR_START] >= start]
        df = df.loc[df[c.YEAR_START] <= end]

    st.subheader(f":blue[Overview per {target}s]", divider="green")
    # allow parameter to get an overview e.g. number, deaths, affected, duration, etc.

    df_target_count = df[target].value_counts()
    target_bar = px.bar(
        df_target_count,
        x=df_target_count.index,
        y='count',
        title=f"Number of Events Worldwide per {target} ({start} to {end})")
    st.plotly_chart(target_bar)

    # TODO: produce one scatter_df with data upload and put in session_state??
    scatter_df = df
    scatter_df[c.DEATHS] = scatter_df[c.DEATHS].fillna(0)

    target_scatter = px.scatter(
        scatter_df,
        x=c.DATE_START,
        y=c.DEATHS,
        color=target,
        hover_data=[c.COUNTRY, c.NUM],
        title=f"Deaths differentiated by {target} ({start} to {end})",
        subtitle="data gaps filled with 0 for visualisation")
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
                target_df = df
                target_df = target_df.loc[target_df[target] == dis_target]

                target_scatter_df = target_df
                target_scatter_df[c.DEATHS] = target_scatter_df[c.DEATHS].fillna(0)

                fig_death = px.scatter(
                    data_frame=target_scatter_df,
                    x=c.DATE_START,
                    y=c.DEATHS,
                    color=c.SUBREGION,
                    title=f"Deaths of {dis_target} differentiated by  {c.SUBREGION} ({start} to {end})",
                    subtitle="data gaps filled with 0 for visualisation",
                    hover_data=[c.COUNTRY, c.YEAR_START, c.NUM])
                st.plotly_chart(fig_death)

                st.write("Explore further parameters:")
                selected_parameter = st.multiselect(label="more parameters",
                                                    options=sorted(c.plot_list),
                                                    label_visibility="collapsed",
                                                    key=f"parameter box {dis_target}")

                # TODO: fix if empty
                for parameter in selected_parameter:
                    st.subheader(f"{parameter}")
                    st.write(f"*{info_dict.get(parameter)}*")

                    if parameter in c.int_list:
                        fig_hist = px.histogram(
                            data_frame=target_df,
                            x=parameter,
                            nbins=30,  # TODO: remove on click max 1% of values
                            title=f"Distribution of {parameter} ({start} to {end})")
                        st.plotly_chart(fig_hist)

                    if parameter in c.info_list:
                        df = treat_text_column(data=target_df, column=parameter)  # drop nan
                        info = f'{', '.join(df[parameter])}'
                        info = pd.Series(info.split(', ')).value_counts()

                        if parameter == c.MONTH_START:
                            info.index = info.index.map(lambda x: month_dict.get(x, x))
                        st.dataframe(
                            data=info,
                            column_config={"count": st.column_config.NumberColumn(label="value count"),
                                           "": st.column_config.TextColumn(label=parameter,
                                                                           width="large")},
                            use_container_width=True)

                    if parameter == c.MAG:
                        agg_mag = target_df.groupby(c.MAG_SCALE).agg(
                            {c.MAG: ['min', 'max', 'mean', np.median]})
                        st.write(agg_mag)  # TODO: switch to dataframe and layout number format

                        fig_hist = px.histogram(
                            data_frame=target_df,
                            x=parameter,
                            nbins=30,
                            title=f"Distribution of {parameter} ({start} to {end})")
                        st.plotly_chart(fig_hist)

                    if parameter in c.att_list:
                        info = target_df[parameter].dropna().unique()
                        st.write(f'Attributed {parameter}(s): {', '.join(info)}')

    st.subheader(f":blue[Compare {target}s per chosen parameter]", divider="green")
    request_subgroups = st.multiselect(label="subgroup for box comparison",
                                       options=sorted(df[target].unique()),
                                       label_visibility="collapsed",
                                       key="subgroup select")

    request_parameter = st.selectbox(label="parameters for box comparison",
                                     options=sorted(c.int_list),
                                     label_visibility="collapsed",
                                     key="parameter select")

    if len(request_subgroups) > 0:
        df["request"] = np.where(df[target].isin(request_subgroups), 'request', 'no')
        df_request = df.loc[df["request"] == "request"]

        with st.container(border=True):
            st.write(f'Definition of :blue[{request_parameter}]: *{info_dict.get(request_parameter)}*')

        q = st.slider(label="*Select restrictive quantile for better visualisation*",
                      min_value=0.00, max_value=1.00, value=1.00)
        mask = df_request[request_parameter].quantile(q)
        df_request.loc[df_request[request_parameter] > mask] = np.nan

        box, hist, table = st.tabs(['Box-Plot', 'Histogram', 'Table'])

        with box:
            event_count = df_request[target].value_counts()

            fig_box = px.box(
                data_frame=df_request,
                x=target,
                y=request_parameter,
                title=f"{request_parameter} per selected {target}",
                subtitle=f"upper {int((1-q)*100)}% of data points removed")

            for cat in request_subgroups:
                fig_box.add_annotation(
                    x=cat,
                    y=df_request[request_parameter].max(),
                    yshift=10,
                    text=f'{str(event_count.get(cat, 0))} events',
                    showarrow=False,
                    font=dict(size=12, color=c.COLOR_NUM_PLOT),
                )
            fig_box.update_layout()
            st.write("")
            st.plotly_chart(fig_box)

        with hist:
            fig_hist = px.histogram(
                data_frame=df_request,
                x=request_parameter,
                color=target,
                barmode='group',
                nbins=30,
                title=f"Distribution of {request_parameter} per selected {target} ({start} to {end})",
                subtitle=f"upper {int((1-q)*100)}% of data points removed")
            st.plotly_chart(fig_hist)

        with table:
            st.write(f"*upper {int((1-q)*100)}% of data points removed*")
            agg_table = df_request.groupby(target).agg({request_parameter : ['sum', 'min', 'max', 'mean', np.median]})
            st.dataframe(
                data=agg_table,
                column_config={
                    1: st.column_config.NumberColumn(
                        label="sum",
                        format="localized"),
                    2: st.column_config.NumberColumn(
                        label="min",
                        format="localized"),
                    3: st.column_config.NumberColumn(
                        label="max",
                        format="localized"),
                    4: st.column_config.NumberColumn(
                        label="mean",
                        format="localized"),
                    5: st.column_config.NumberColumn(
                        label="median",
                        format="localized")})

st.divider()
st.write(TEXT_IMPRESSUM)
