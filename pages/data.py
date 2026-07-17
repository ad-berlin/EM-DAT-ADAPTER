import streamlit as st
import plotly.express as px
import pandas as pd

from text import text_info as t
from utils import modules as m
from utils import constants as c

st.subheader(t.HEADER, divider="grey")

if 'data' not in st.session_state:
    st.error(t.ERROR_DATA)

else:
    df = st.session_state['data'].copy()

    add_col_current_entry = "Entry Delay in Days"
    df[add_col_current_entry] = (df[c.ENTRY_DATE] - df[c.DATE_START]).dt.days
    add_col_entry_year = "Year of Entry"
    df[add_col_entry_year] = df[c.ENTRY_DATE].dt.year

    with st.container(border=True):
        start, end = m.write_time(data=df)
        df = df.loc[df[c.YEAR_START] >= start]
        df = df.loc[df[c.YEAR_START] <= end]

    with st.container(border=True):  # Distribution across Variables
        st.write(":blue[Distribution across Variables]")
        dis_subtype_sorted = [x for _, x in sorted(zip(df[c.DIS_TYPE], df[c.DIS_SUBTYPE]))]
        dis_subtype_order = pd.Series(dis_subtype_sorted).unique()

        dis_type_order = sorted(df[c.DIS_TYPE].unique())

        subregion_sorted = [x for _, x in sorted(zip(df[c.OPT_REGION], df[c.OPT_SUBREGION]))]
        subregion_order = pd.Series(subregion_sorted).unique()

        region_order = sorted(df[c.OPT_REGION].unique())

        order_dict = {
            c.OPT_REGION: region_order,
            c.OPT_SUBREGION: subregion_order,
            c.DIS_TYPE: dis_type_order,
            c.DIS_SUBTYPE: dis_subtype_order
        }

        for x, y in [(c.DIS_TYPE, c.OPT_REGION), (c.DIS_TYPE, c.OPT_SUBREGION), (c.DIS_SUBTYPE, c.OPT_REGION),
                     (c.DIS_SUBTYPE, c.OPT_SUBREGION)]:
            with st.expander(f"{x} x {y}"):
                fig = px.density_heatmap(df, x=x, y=y, text_auto=True, color_continuous_scale='Viridis',
                                         category_orders={x: order_dict.get(x),
                                                          y: order_dict.get(y)},
                                         title=f"Distribution across Variables - {x} x {y}")
                st.plotly_chart(fig)

    with st.container(border=True):  # General Database Structure
        st.write(":blue[Indicators of General Database Structure]")
        with st.expander("Update Structure"):
            fig = px.histogram(df, x=c.UPDATE_DATE, log_y=True, title=f"{c.UPDATE_DATE} Count")
            fig.update_layout(bargap=0.2)
            st.plotly_chart(fig)

            fig = px.density_heatmap(
                df,
                y=c.YEAR_START,
                x=c.UPDATE_DATE,
                color_continuous_scale="Viridis",
                text_auto=True,
                title=f"{c.YEAR_START} per {c.UPDATE_DATE}"
            )
            st.plotly_chart(fig)

        with st.expander("Recency of Entry"):
            fig = px.scatter(
                df,
                y=add_col_current_entry,
                x=c.YEAR_START,
                color=add_col_entry_year,
                color_continuous_scale="Viridis",
                title=f"{add_col_current_entry} per {c.YEAR_START} differentiated by {add_col_entry_year}"
            )
            st.plotly_chart(fig)

            temp_df = df.loc[
                (df[add_col_current_entry] <= 365) & (df[add_col_current_entry] >= 0)]
            fig = px.box(
                temp_df,
                y=add_col_current_entry,
                x=c.YEAR_START,
                title=f"{add_col_current_entry}, lower 365 days, per {c.YEAR_START}"
            )
            st.plotly_chart(fig)

            st.write(
                f"Entries with an Entry Date before an Event Date ({len(df.loc[df[add_col_current_entry] < 0])} Events)")
            result_df = df.loc[df[add_col_current_entry] < 0][
                [c.NUM, c.YEAR_START, c.MONTH_START, c.DAY_START, c.ENTRY_DATE, c.UPDATE_DATE,
                 add_col_current_entry]]
            st.dataframe(result_df, hide_index=True)

        with st.expander("Definition Discrepancy"):
            st.write(t.COHERENCE_TEXT)
            human_impact_cols = [c.DEATHS, c.AFFECTED, c.HOMELESS]
            test_col = "Sum Human Impact Columns"
            df[test_col] = df[human_impact_cols].sum(axis=1)
            temp_df = df.loc[(df[test_col] != 0) & (df[test_col].notna())]
            fig = px.scatter(
                temp_df,
                y=test_col,
                x=c.TOT_AFFECTED,
                color=c.AFFECTED,
                log_y=True,
                log_x=True,
                color_continuous_scale="Purp_r",
                title=f"{round(len(temp_df) / len(df) * 100, 2)}% of all Values show a difference between Sum Human Impact Columns and Total Affected",
                subtitle=f"Of which {round(len(temp_df.loc[temp_df[c.AFFECTED].isna()]) / len(df) * 100, 2)}% {c.AFFECTED} is NaN")
            st.plotly_chart(fig)

        with st.expander("Index Structure"):
            fig = px.scatter(
                df,
                x=df.index,
                y=c.UPDATE_DATE,
                color=add_col_entry_year,
                color_continuous_scale="Viridis",
                title="Index Sorting differentiated by Year of Entry"
            )
            st.plotly_chart(fig)

            fig = px.scatter(
                df,
                x=df.index,
                y=c.DATE_START,
                color=add_col_entry_year,
                color_continuous_scale="Viridis",
                title="Index Sorting differentiated by Year of Entry"
            )
            st.plotly_chart(fig)

            fig = px.scatter(
                df,
                x=df.index,
                y=add_col_entry_year,
                color=add_col_entry_year,
                color_continuous_scale="Viridis",
                title="Index Sorting differentiated by Year of Entry"
            )
            st.plotly_chart(fig)

    with st.container(border=True):  # Missingness and Its Patterns
        st.write(":blue[Missingness and Its Patterns]")
        complete_list = []
        lacking_list = []
        plot_list = []
        total_events = len(df)
        for col in c.original_list:
            df[col] = df[col].fillna("no data")

            val_count = df[col].value_counts()
            if "no data" in val_count:
                perc = df[col].value_counts()["no data"] / total_events
                lacking_list.append(f"{col} ({round(perc * 100, 2)}%)")
                plot_list.append((col, perc * 100))
            else:
                complete_list.append(col)


        with st.expander(label="Incomplete Columns"):
            fig = px.bar(plot_list,
                         x=0, y=1,
                         color=1,
                         color_continuous_scale="Reds",
                         title=f"Missing Data per Column [%] ({start}-{end})")
            fig.update_layout(yaxis_title="Percent Missing Data", xaxis_title="")
            fig.update_coloraxes(showscale=False)
            st.plotly_chart(fig)

        with st.expander(label="Complete Columns"):
            st.dataframe(complete_list)

        interesting_list = [c.ORIGIN, c.ASS_TYPES, c.MAG, c.AID, c.DAMAGE, c.RECONSTRUCTION, c.INSURED, c.DEATHS,
                            c.INJURED, c.AFFECTED, c.HOMELESS]

        with st.expander(label=f"Missingness per {c.DIS_TYPE}"):
            col = st.selectbox("Column of Missingness", options=interesting_list, key="col_select_type")
            fig_df_dict = df[c.DIS_TYPE].value_counts()  # list of event count per geo-SR
            temp_df = df.loc[df[col] == "no data"]  # filter to "no data" for interesting col
            fig_df = temp_df[c.DIS_TYPE].value_counts()  # list of event count per geo-SR with "no data"

            plot_lst = []
            for location in temp_df[c.DIS_TYPE].unique():
                perc = fig_df[location] / fig_df_dict.get(location)  # divide "no data" through all events
                plot_lst.append((location, perc * 100))

            fig = px.bar(plot_lst,
                         x=0, y=1,
                         color=1,
                         color_continuous_scale="Reds",
                         title=f"Missing Data for {col} ({start}-{end})")
            fig.update_layout(yaxis_title="Percent Missing Data", xaxis_title="")
            fig.update_coloraxes(showscale=False)
            st.plotly_chart(fig)

        with st.expander(label=f"Missingness per {c.GEOGRAPH_SR}"):
            col = st.selectbox("Column of Missingness", options=interesting_list, key="col_select_region")
            fig_df_dict = df[c.GEOGRAPH_SR].value_counts()  # list of event count per geo-SR
            temp_df = df.loc[df[col] == "no data"]  # filter to "no data" for interesting col
            fig_df = temp_df[c.GEOGRAPH_SR].value_counts()  # list of event count per geo-SR with "no data"

            plot_lst = []
            for location in temp_df[c.GEOGRAPH_SR].unique():
                perc = fig_df[location] / fig_df_dict.get(location)  # divide "no data" through all events
                plot_lst.append((location, perc * 100))

            fig = px.bar(plot_lst,
                         x=0, y=1,
                         color=1,
                         color_continuous_scale="Reds",
                         title=f"Missing Data for {col} ({start}-{end})")
            fig.update_layout(yaxis_title="Percent Missing Data", xaxis_title="")
            fig.update_coloraxes(showscale=False)
            st.plotly_chart(fig)

        with st.expander(label=f"Missingness per {c.YEAR_START}"):
            col = st.selectbox("Column of Missingness", options=interesting_list, key="col_select_year")
            fig_df_dict = df[c.YEAR_START].value_counts()  # list of event count per start year
            temp_df = df.loc[df[col] == "no data"]  # filter to "no data" for interesting col
            fig_df = temp_df[c.YEAR_START].value_counts()  # list of event count per start year with "no data"

            plot_lst = []
            for location in temp_df[c.YEAR_START].unique():
                perc = fig_df[location] / fig_df_dict.get(location)  # divide "no data" through all events
                plot_lst.append((location, perc * 100))

            fig = px.bar(plot_lst,
                         x=0, y=1,
                         color=1,
                         color_continuous_scale="Reds",
                         title=f"Missing Data for {col} ({start}-{end})")
            fig.update_layout(yaxis_title="Percent Missing Data", xaxis_title="")
            fig.update_coloraxes(showscale=False)
            st.plotly_chart(fig)

m.write_impressum()
