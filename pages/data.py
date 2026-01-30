import streamlit as st
import plotly.express as px


from text import text_info as t
from utils import modules as m
from utils import constants as c

st.subheader(t.HEADER, divider="grey")

if 'data' not in st.session_state:
    st.error(t.ERROR_DATA)

else:
    df = st.session_state['data'].copy()

    m.write_help(page_in_capitals='DIS_TYPE')
    with st.container(border=True):
        start, end = m.write_time(data=df)
        df = df.loc[df[c.YEAR_START] >= start]
        df = df.loc[df[c.YEAR_START] <= end]

    # with st.container(border=True):  # TODO??
    #     for reg in df[c.REGION].unique():
    #         list_reg = df.loc[df[c.REGION] == reg][c.COUNTRY].value_counts()[0:7]
    #         st.write(reg)
    #         st.write(list_reg)
    #         for country in list_reg.index[0:7]:
    #             col1, col2 = st.columns(2)
    #             col1.write(country)
    #             col2.write(df.loc[df[c.COUNTRY] == country][c.DIS_SUBTYPE].value_counts()[0:5])

    with st.container(border=True):
        complete_list = []
        lacking_list = []
        plot_list = []
        total_events = len(df)
        for col in df.columns:
            df[col] = df[col].fillna("no data")

            val_count = df[col].value_counts()
            if "no data" in val_count:
                perc = df[col].value_counts()["no data"] / total_events
                lacking_list.append(f"{col} ({round(perc * 100, 2)}%)")
                plot_list.append((col, perc * 100))
            else:
                complete_list.append(col)


        with st.expander(label="Lacking Columns"):
            fig = px.bar(plot_list, x=0, y=1, title=f"Missing Data per Column [%] ({start}-{end})")
            fig.update_layout(yaxis_title="Percent Missing Data", xaxis_title="")
            st.plotly_chart(fig)

        with st.expander(label="Complete Columns"):
            st.dataframe(complete_list)

    with st.container(border=True):
        interesting_list = [c.ORIGIN, c.ASS_TYPES, c.MAG, c.AID, c.DAMAGE, c.RECONSTRUCTION, c.INSURED, c.DEATHS,
                            c.INJURED, c.AFFECTED, c.HOMELESS]

        with st.expander(label=f"Lacking Data per {c.DIS_TYPE}"):
            for col in interesting_list:
                fig_df_dict = df[c.DIS_TYPE].value_counts()  # list of event count per geo-SR
                temp_df = df.loc[df[col] == "no data"]  # filter to "no data" for interesting col
                fig_df = temp_df[c.DIS_TYPE].value_counts()  # list of event count per geo-SR with "no data"

                plot_lst = []
                for location in temp_df[c.DIS_TYPE].unique():
                    perc = fig_df[location] / fig_df_dict.get(location)  # divide "no data" through all events
                    plot_lst.append((location, perc * 100))

                fig = px.bar(plot_lst, x=0, y=1, title=f"Missing Data for {col} ({start}-{end})")
                fig.update_layout(yaxis_title="Percent Missing Data", xaxis_title="")
                st.plotly_chart(fig)

        with st.expander(label=f"Lacking Data per {c.GEOGRAPH_SR}"):
            for col in interesting_list:
                fig_df_dict = df[c.GEOGRAPH_SR].value_counts()  # list of event count per geo-SR
                temp_df = df.loc[df[col] == "no data"]  # filter to "no data" for interesting col
                fig_df = temp_df[c.GEOGRAPH_SR].value_counts()  # list of event count per geo-SR with "no data"

                plot_lst = []
                for location in temp_df[c.GEOGRAPH_SR].unique():
                    perc = fig_df[location] / fig_df_dict.get(location)  # divide "no data" through all events
                    plot_lst.append((location, perc * 100))

                fig = px.bar(plot_lst, x=0, y=1, title=f"Missing Data for {col} ({start}-{end})")
                fig.update_layout(yaxis_title="Percent Missing Data", xaxis_title="")
                st.plotly_chart(fig)

        with st.expander(label=f"Lacking Data per {c.YEAR_START}"):
            for col in interesting_list:
                fig_df_dict = df[c.YEAR_START].value_counts()  # list of event count per start year
                temp_df = df.loc[df[col] == "no data"]  # filter to "no data" for interesting col
                fig_df = temp_df[c.YEAR_START].value_counts()  # list of event count per start year with "no data"

                plot_lst = []
                for location in temp_df[c.YEAR_START].unique():
                    perc = fig_df[location] / fig_df_dict.get(location)  # divide "no data" through all events
                    plot_lst.append((location, perc * 100))

                fig = px.bar(plot_lst, x=0, y=1, title=f"Missing Data for {col} ({start}-{end})")
                fig.update_layout(yaxis_title="Percent Missing Data", xaxis_title="")
                st.plotly_chart(fig)

m.write_impressum()
