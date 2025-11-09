import streamlit as st
import plotly.express as px

from utils import constants as c
from utils import modules as m
from utils import ut as u
from text import text_info as t

st.subheader(t.HEADER, divider="grey")

with st.container(border=True):
    st.write(':blue[Step 1]')
    st.write('The data is saved for processing as you upload it. Interested how that data looks like?')
    with st.expander("EM-DAT raw data"):
        if 'data' not in st.session_state:
            st.error(t.ERROR_DATA)
        else:
            df = st.session_state['data'].copy()
            st.write("The original EM-DAT file filtered for the Disaster Group 'Natural'")
            st.dataframe(data=df[c.original_list], hide_index=True)

with st.container(border=True):
    st.write(':blue[Step 2]')
    st.write('Additional columns are added and missing dates are treated. Interested what columns are new and why?')
    with st.expander("List of new columns"):
        for col in c.new_list:
            st.write(f"""
            :blue[{col}]: {t.info_dict.get(col)}  
            {t.explain_dict.get(col)}""")
        st.write('For mor information regarding the definitions of the Regions/Subregions/Countries, explore the sources.')

with st.container(border=True):
    st.write(':blue[Step 3]')
    st.write(f"The column '{c.ORIGIN}' and '{c.LOCATION}' are treated. Interested why and how?")
    with st.expander(f"Special needs columns"):
        st.write(f":blue[The column '{c.ORIGIN}']")
        st.write("To be filled...")
        st.write(f":blue[The column '{c.LOCATION}']")
        st.write("To be filled...")

with st.container(border=True):
    st.write(':blue[Step 4]')
    st.write(f"The numeric columns are treated to be visualized in scatter plots. Interested why and how?")
    with st.expander("Scatter plot treatment"):
        if 'data' not in st.session_state:
            st.error(t.ERROR_DATA)
        else:
            df = st.session_state['data'].copy()
            df = df.loc[df[c.YEAR_START] >= df[c.YEAR_START].max() - 5]
            df = df.loc[df[c.YEAR_START] <= df[c.YEAR_START].max()]

            target = c.HOMELESS

            st.write("Data is lacking. To see that please check out the page on Data Quality.")
            st.write("But still somehow there should be a way to show all the events spread over time. "
                     "That's why the data gaps are temporarily filled with 0 to allow a painted dot in the scatter plot. "
                     "This feature can be disabled in the analysis page 'Explore Further', where you can build your own plots.")

            chosen_continent = st.selectbox(t.SELECT_REGION, options=df[c.CONTINENT_R].unique())
            df = df.loc[df[c.CONTINENT_R] == chosen_continent]

            st.write(f"""
            Here an example over five years over {target} ({chosen_continent}):  
            - {df[target].count()} entries,
            - {len(df)} entries missing,
            - only {round(df[target].count()/len(df), 2) * 100}% have existing data!
            """)

            col1, col2 = st.columns(2)

            target_scatter = px.scatter(
                u.build_scatter_data(df),
                x=c.DATE_START,
                y=target,
                title=f"{target} in {chosen_continent} ({df[c.YEAR_START].max() - 5} to {df[c.YEAR_START].max()})",
                subtitle="data gaps filled with 0 for visualisation")
            col1.plotly_chart(target_scatter)

            target_scatter = px.scatter(
                df,
                x=c.DATE_START,
                y=target,
                title=f"{target} in {chosen_continent} ({df[c.YEAR_START].max() - 5} to {df[c.YEAR_START].max()})",
                subtitle="data gaps NOT filled")
            col2.plotly_chart(target_scatter)


with st.container(border=True):
    st.write(':blue[Step 5]')
    st.write(f"The data is made visible in multiple pages. Interested to make it better?")
    with st.expander("How to improve DisTrack"):
        st.write('''
        The process of building an up-to-date visualisation tool (sadly or luckily?) never ends. Constant improvements
        keep the tool active and allow insightful analysis. These improvements need to be community-driven to be useful.
        Therefore your participation is needed.
        
        :violet[Find out more about how to participate!]
        ''')

m.write_impressum()
