import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
from unidecode import unidecode

from text import text_info as t
from utils import constants as c
from utils import ut as u


def write_help(page_in_capitals) -> None:
    with st.expander(t.TEXT_HELP, icon=':material/info:'):
        st.markdown(t.help_dict.get(f'HELP_{page_in_capitals}'))


def write_impressum() -> None:
    st.divider()
    st.write(t.TEXT_IMPRESSUM)


def write_time(data):
    latest_year = data[c.YEAR_START].max()
    earliest_year = data[c.YEAR_START].min()
    all_years = sorted(data[c.YEAR_START].unique())

    st.write(f":blue[{t.SELECT_TIME}]")
    start, end = st.select_slider(label=t.SELECT_TIME,
                                  options=all_years,
                                  value=(earliest_year, latest_year),
                                  label_visibility="collapsed")
    return start, end


def write_overview(target, data, start, end, hover_list) -> None:
    st.write(f":blue[I want to get an overview per {target}]")
    y_scatter = st.selectbox(label=f"{t.SELECT_PARAM_OV}",
                             options=sorted(c.overview_list))
    with st.container(border=True):
        st.write(f'Definition of :blue[{y_scatter}]: {t.info_dict.get(y_scatter)}')

    if y_scatter == c.NUMBER_EV:
        df_target_count = data[target].value_counts()
        target_bar = px.bar(
            df_target_count,
            x=df_target_count.index,
            y='count',
            title=f"Number of Events Worldwide per {target} ({start} to {end})")
        st.plotly_chart(target_bar)
    else:
        target_scatter = px.scatter(
            u.build_scatter_data(data),
            x=c.DATE_START,
            y=y_scatter,
            color=target,
            category_orders={target: sorted(u.build_scatter_data(data)[target].dropna().unique())},
            hover_data=hover_list,
            title=f"{y_scatter} differentiated by {target} ({start} to {end})",
            subtitle="data gaps filled with 0 for visualisation")
        st.plotly_chart(target_scatter)


def write_dig_deep(target, data, start, end, filter=False, filter_cat=None):
    if target != c.OPT_COUNTRY:
        target_plural = f"{target}s"
    else:
        target_plural = "EM-DAT Countries"

    if filter and filter_cat:
        added_filter = st.selectbox(label="subgroup for box comparison",
                                    options=sorted(data[filter_cat].fillna("no data").unique()),
                                    placeholder=f"Choose {c.DIS_TYPE}s for comparison",
                                    label_visibility="collapsed",
                                    key="dis_type select deep analysis")
        data = data.loc[data[filter_cat] == added_filter]

    selected_subtargets = st.multiselect(label=f"certain {target} select",
                                         options=sorted(data[target].fillna("no data").unique()),
                                         placeholder=f"Choose {target_plural}",
                                         label_visibility="collapsed")
    if len(selected_subtargets) > 0:
        tabs = st.tabs(selected_subtargets)

        for ix, dis_target in enumerate(selected_subtargets):
            with tabs[ix]:
                target_df = data.copy()
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
                            if len(target_df[parameter].unique()) < 3:
                                st.error(t.ERROR_VALUE)
                            else:
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
                                    data_frame=u.build_scatter_data(target_df),
                                    x=c.DATE_START,
                                    y=parameter,
                                    title=f"{parameter} of {dis_target} ({start} to {end})",
                                    subtitle=f"data gaps filled with 0 for visualisation; upper {int((1 - q_1) * 100)}% of data points removed",
                                    hover_data=[c.YEAR_START, c.NUM, c.DIS_SUBTYPE])
                                col2.plotly_chart(fig_scatter)

                        if parameter == c.MONTH_START:
                            info = target_df[c.MONTH_START].value_counts()
                            info.index = info.index.map(lambda x: t.month_dict.get(x, x))
                            st.dataframe(
                                data=info,
                                column_config={"count": st.column_config.NumberColumn(label="Value Count"),
                                               c.MONTH_START: st.column_config.TextColumn(label=parameter,
                                                                               width="large")},
                                use_container_width=True)

                        if parameter in c.info_list:  # TODO: fix presentation
                            target_df = u.treat_text_column(data=target_df, columns=[parameter])
                            info = f"{', '.join(target_df[parameter])}"
                            info = pd.Series(info.split(', ')).value_counts()

                            st.dataframe(
                                data=info,
                                column_config={"count": st.column_config.NumberColumn(label="Value Count"),
                                               "": st.column_config.TextColumn(label=parameter,
                                                                               width="large")},
                                use_container_width=True)

                        # if parameter in c.att_list:
                        #     info = target_df[parameter].dropna().unique()
                        #     st.write(f"Attributed {parameter}(s): {', '.join(info)}")

                        if parameter in c.att_list:
                            info = target_df[parameter].value_counts()
                            st.dataframe(
                                data=info,
                                column_config={"count": st.column_config.NumberColumn(label="Value Count"),
                                               "": st.column_config.TextColumn(label=parameter,
                                                                               width="large")},
                                use_container_width=True)


                        st.write(f"*{t.info_dict.get(parameter)}")
    return target


def write_compare(target, data, start, end, filter=False, filter_cat=None):
    if target != c.OPT_COUNTRY:
        target_plural = f"{target}s"
    else:
        target_plural = "EM-DAT Countries"

    if filter and filter_cat:
        added_filter = st.selectbox(label="subgroup for box comparison",
                                    options=sorted(data[filter_cat].fillna("no data").unique()),
                                    placeholder=f"Choose {c.DIS_TYPE}s for Comparison",
                                    label_visibility="collapsed",
                                    key="dis_type select compare")
        data = data.loc[data[filter_cat] == added_filter]

    request_subgroups = st.multiselect(label="subgroup for box comparison",
                                       options=sorted(data[target].fillna("no data").unique()),
                                       placeholder=f"Choose {target_plural} for Comparison",
                                       label_visibility="collapsed",
                                       key="subgroup select")

    request_parameter = st.selectbox(label=t.SELECT_PARAM_COM,
                                     options=sorted(c.int_list),
                                     key="parameter select")

    if len(request_subgroups) > 0:
        data["request"] = np.where(data[target].isin(request_subgroups), 'request', 'no')
        df_request = data.loc[data["request"] == "request"]

        with st.container(border=True):
            st.write(f'Definition of :blue[{request_parameter}]: *{t.info_dict.get(request_parameter)}*')

        q_2 = st.slider(label="*Select restrictive quantile for better visualisation*",
                        min_value=0.00, max_value=1.00, value=1.00)
        mask_2 = df_request[request_parameter].quantile(q_2)
        df_request.loc[df_request[request_parameter] > mask_2] = np.nan

        box, hist, table = st.tabs(['Box-Plot', 'Histogram', 'Table'])

        with box:
            event_count = df_request[target].value_counts()

            fig_box = px.box(
                data_frame=df_request,
                x=target,
                y=request_parameter,
                title=f"{request_parameter} per selected {target} ({start} to {end})",
                subtitle=f"upper {int((1 - q_2) * 100)}% of data points removed")

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
                subtitle=f"upper {int((1 - q_2) * 100)}% of data points removed")
            st.plotly_chart(fig_hist)

        with table:
            st.write(f"*upper {int((1 - q_2) * 100)}% of data points removed*")
            agg_table = df_request.groupby(target).agg({request_parameter: ['sum', 'min', 'max', 'mean', np.median]})
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

    return target


def build_filter(data):
    info = []
    filter_params = st.multiselect(label="params for filter",
                                   options=sorted(c.filter_list),
                                   label_visibility="collapsed",
                                   placeholder="Choose parameters for filter options")
    for param in filter_params:
        st.write(f"Filter :blue[{param}]")

        if param is c.ORIGIN_LABEL:
            options_list = "; ".join(data[param])
            options_list = pd.Series(options_list.split("; ")).unique()
            argument = st.multiselect(label=f"{param} to filter",
                                      options=options_list,
                                      label_visibility="collapsed")

            for i, arg in enumerate(argument):
                if "(" in arg:
                    argument[i] = arg.split(" ")[0]

            pattern = "|".join(argument)
            data = data.loc[data[param].str.contains(pattern, na=False)]  # na=False: treat NaN as False
            info.append((param, ', '.join(argument)))

        elif param in c.int_list or param in c.date_list:
            col1, col2 = st.columns([4,1])
            min_val, max_val = col1.select_slider(label=f"{param} to filter",
                                                options=sorted(data[param].fillna(data[param].min()).unique()),
                                                value=(data[param].min(), data[param].max()),
                                                label_visibility="collapsed")
            filtered = data[(data[param] >= min_val) & (data[param] <= max_val)]

            show_nan = col2.toggle("show nan values", key=f"{param}_toggl")
            if show_nan:
                nan_rows = data[data[param].isna()]
                data = pd.concat([filtered, nan_rows], axis=0)
                info.append((param, f"{min_val} to {max_val}, incl. nan"))

            else:
                data = filtered
                info.append((param, f"{min_val} to {max_val}"))

        elif param in c.text_field_list:
            data = u.treat_text_column(data=data, columns=[param], new=True)

            argument = st.text_input(label=f"{param} to filter",
                                     placeholder="Please type what you look for",
                                     label_visibility="collapsed")
            argument = unidecode(argument.lower())
            data = data.loc[data[f"{param} (assist)"].str.contains(argument, na=False)]  # na=False: treat NaN as False
            data = data.drop(columns=[f"{param} (assist)"])
            info.append((param, f"cell contains {argument}"))

        else:
            argument = st.multiselect(label=f"{param} to filter",
                                      options=data[param].unique(),
                                      label_visibility="collapsed")

            for i, arg in enumerate(argument):
                if "(" in arg:
                    argument[i] = arg.split(" ")[0]

            pattern = "|".join(argument)
            data = data.loc[data[param].str.contains(pattern, na=False)]  # na=False: treat NaN as False
            info.append((param, ', '.join(argument)))

    info = pd.DataFrame(info)
    return data, info
