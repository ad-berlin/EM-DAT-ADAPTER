import streamlit as st

from text.text_info import TEXT_INTRO
from utils.utils import get_data, get_un_data
from text.text_info import TEXT_IMPRESSUM


st.header(":violet[EM-DAT: Visualising International Disaster]", divider="rainbow")

st.write(TEXT_INTRO)

st.write(":red[Please be patient for the upload...]")

# EM-DAT data
file_upload_em = st.file_uploader(
    "*Upload your EM-DAT xlsx file...*",
    type=['xlsx'])

if file_upload_em:
    st.session_state['data'] = get_data(file=file_upload_em)

if 'data' in st.session_state:
    st.success("EM-DAT file upload successful!")

# UN data
on = st.toggle("Enable additional upload UN population data", key="un_toggle")
if on:
    file_upload_un = st.file_uploader(
        "*Upload your UN csv file...*",
        type=['csv'])

    if file_upload_un:
        st.session_state['un_data'] = get_un_data(file=file_upload_un)

if 'un_data' in st.session_state:
    st.success("UN file upload successful!")


st.divider()
st.write(TEXT_IMPRESSUM)

