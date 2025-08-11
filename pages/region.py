import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd

from utils import constants as c
from utils import modules as m
from text.text_info import info_dict, error_dict, select_dict, TEXT_IMPRESSUM, month_dict
from utils.ut import treat_text_column, build_scatter_data

# specific page constants todo: add to constants
KEY_REGION_SPEC = 'region_specification'
KEY_SUBREGION_SPEC = 'subregion_specification'
KEY_COUNTRY_SPEC = 'country_specification'

OPT_COUNTRY = 'EM-DAT Countries'

LST_REGION = [c.CONTINENT, c.UN_M49_R]
LST_SUBREGION = [c.GEOGRAPH_R, c.UN_M49_SUBR]
LST_COUNTRY = [c.SOVEREIGN_C, OPT_COUNTRY, c.ADMIN_C, c.UN_M49_C]

if 'data' not in st.session_state:
    st.error(error_dict.get('ERROR_DATA'))

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

    latest_year = df[c.YEAR_START].max()
    earliest_year = df[c.YEAR_START].min()
    all_years = sorted(df[c.YEAR_START].unique())

    # start actual content
    m.write_help(page_in_capitals='REGION')

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

        st.write(select_dict.get('SELECT_TIME'))
        start, end = st.select_slider(label="timespan_region",
                                      options=sorted(all_years),
                                      value=(earliest_year, latest_year),
                                      label_visibility="collapsed")
        df = df.loc[df[c.YEAR_START] >= start]
        df = df.loc[df[c.YEAR_START] <= end]

    with st.container(border=True):
        st.write(f'''
        :blue[I want to get an overview per {target}*...]  
        *{spec}
        ''')

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

    with st.container(border=True):
        if target != "Country":
            target_plural = f"{target}s"
        else:
            target_plural = "Countries"

        st.write(f":blue[I want to find out more about certain {target_plural}...]")
        selected_subtargets = st.multiselect(label=f"certain {target} select",
                                             options=sorted(df[target].unique()),
                                             placeholder=f"Choose {target_plural}",
                                             label_visibility="collapsed")
        if len(selected_subtargets) > 0:
            tabs = st.tabs(selected_subtargets)

            for ix, dis_target in enumerate(selected_subtargets):
                with tabs[ix]:
                    target_df = df
                    target_df = target_df.loc[target_df[target] == dis_target]

                    selected_parameter = st.multiselect(label=f"params for exploration",
                                                        options=sorted(c.plot_list),
                                                        placeholder="Choose parameters for exploration",
                                                        key=f"parameter box {dis_target} page region",
                                                        label_visibility="collapsed")

                    for parameter in selected_parameter:
                        with st.container(border=True):
                            st.write(f":violet[{parameter}*]")

                            if parameter in c.int_list:
                                if parameter == c.MAG:
                                    agg_mag = target_df.groupby(c.MAG_SCALE).agg(
                                        {c.MAG: ['min', 'max', 'mean', np.median]})
                                    st.write(agg_mag)  # TODO: switch to dataframe and layout number format

                                q_1 = st.slider(label="Select restrictive quantile for better visualisation",
                                                min_value=0.00, max_value=1.00, value=1.00,
                                                key=f"q1_slider_{parameter}_{dis_target}")
                                mask_1 = target_df[parameter].quantile(q_1)
                                target_df.loc[target_df[parameter] > mask_1] = np.nan

                                col1, col2 = st.columns(2)
                                fig_hist = px.histogram(
                                    data_frame=target_df,
                                    x=parameter,
                                    nbins=30,
                                    title=f"Distribution of {parameter} of {dis_target} ({start} to {end})",
                                    subtitle=f"upper {int((1 - q_1) * 100)}% of data points removed")
                                col1.plotly_chart(fig_hist)

                                fig_scatter = px.scatter(
                                    data_frame=build_scatter_data(target_df),
                                    x=c.DATE_START,
                                    y=parameter,
                                    title=f"{parameter} of {dis_target} ({start} to {end})",
                                    subtitle=f"data gaps filled with 0 for visualisation; upper {int((1 - q_1) * 100)}% of data points removed",
                                    hover_data=[c.COUNTRY, c.YEAR_START, c.NUM])
                                col2.plotly_chart(fig_scatter)

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

                            if parameter in c.att_list:
                                info = target_df[parameter].dropna().unique()
                                st.write(f'Attributed {parameter}(s): {', '.join(info)}')

                            st.write(f"*{info_dict.get(parameter)}")


                    if 'un_data' in st.session_state:
                        un_df = st.session_state['un_data'].copy()
                        un_df = un_df.loc[un_df['Time'] >= start]
                        un_df = un_df.loc[un_df['Time'] <= end]
                        info = un_df.loc[un_df['Location'].str.contains(selected_subtargets)]  # TODO: fix weird categories
                        st.dataframe(info)

st.divider()
st.write(TEXT_IMPRESSUM)
