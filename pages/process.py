import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd

from utils import constants as c
from utils import modules as m
from text.text_info import info_dict, error_dict, select_dict, TEXT_IMPRESSUM, month_dict
from utils.ut import treat_text_column, build_scatter_data

with st.container(border=True):
    st.write(':blue[Step 1]')
    st.write('The data is saved for processing as you upload it. Interested how that data looks like?')
    with st.expander("EM-DAT raw data"):
        if 'data' not in st.session_state:
            st.error(error_dict.get('ERROR_DATA'))
        else:
            df = st.session_state['data'].copy()
            st.write("The original EM-DAT file filtered for the Disaster Group 'Natural'")
            st.dataframe(data=df, hide_index=True)

with st.container(border=True):
    st.write(':blue[Step 2]')
    st.write('Additional columns are added and missing dates are treated. Interested what columns are new and why?')
    with st.expander("List of new columns"):
        st.write("to be filled...")

with st.container(border=True):
    st.write(':blue[Step 3]')
    st.write(f"The column '{c.ORIGIN}' and '{c.LOCATION}' are treated. Interested why and how?")
    with st.expander(f"Special needs columns"):
        st.write(f"The column '{c.ORIGIN}'")
        st.write(f"The column '{c.LOCATION}'")

with st.container(border=True):
    st.write(':blue[Step 4]')
    st.write(f"The numeric columns are treated to be visualized in scatter plots. Interested why and how?")
    with st.expander("Scatter plot treatment"):
        st.write("to be filled (plus example)...")

with st.container(border=True):
    st.write(':blue[Step 5]')
    st.write(f"The data is made visible in multiple pages. Interested to make it better?")
    with st.expander("How to improve DisTrack"):
        st.write("to be filled...")



st.divider()
st.write(TEXT_IMPRESSUM)