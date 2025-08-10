import streamlit as st

from text.text_info import TEXT_INTRO
from utils.ut import get_data, get_un_data
from text.text_info import TEXT_IMPRESSUM


st.header(":blue[DisTrack - International Disaster Analysis]", divider="grey")

with st.container(border=True):
    st.write(TEXT_INTRO)

# EM-DAT data
file_upload_em = st.file_uploader(
    "Upload your EM-DAT xlsx file...",
    type=['xlsx'])

if file_upload_em:
    st.session_state['data'] = get_data(file=file_upload_em)

if 'data' in st.session_state:
    st.success("EM-DAT file upload successful!")

# UN data
allow_un_upload = st.toggle("Enable additional upload UN population data", key="un_toggle")
if allow_un_upload:
    file_upload_un = st.file_uploader(
        "Upload your UN csv file...",
        type=['csv'])

    if file_upload_un:
        st.session_state['un_data'] = get_un_data(file=file_upload_un)

if 'un_data' in st.session_state:
    st.success("UN file upload successful!")


st.divider()
st.write(TEXT_IMPRESSUM)
