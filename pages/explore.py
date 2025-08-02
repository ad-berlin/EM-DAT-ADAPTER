import streamlit as st
import plotly.express as px
import pandas as pd

from utils import constants as c
from text.text_info import TEXT_IMPRESSUM, error_dict, select_dict, month_dict
from utils.ut import write_help, treat_text_column, build_scatter_data

if 'data' not in st.session_state:
    st.error(error_dict.get('ERROR_DATA'))

else:
    df = st.session_state['data'].copy()

    write_help(page_in_capitals='EXPLORE')

    st.write(df[c.ORIGIN].value_counts())

    df = treat_text_column(data=df, column=c.ORIGIN)  # drop nan
    info = f'{', '.join(df[c.ORIGIN])}'
    info = pd.Series(info.split(', ')).value_counts()
    st.write(info)


with st.container(border=True):
    st.write('test123')
    with st.container(border=True):
        with st.container(border=True):
            st.write("test123")
            with st.container(border=True):
                st.write("test123")
                col1, col2, col3 = st.columns(3)
                with col1.container(border=True):
                    st.write("test123")
                with col2.container(border=True):
                    st.write("test123")
                with col3.container(border=True):
                    st.write("test123")

st.divider()
st.write(TEXT_IMPRESSUM)
