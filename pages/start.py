import streamlit as st

from utils import constants as c
from utils import modules as m
from utils import ut as u
from text import text_info as t


st.subheader(":blue[DisTrack - International Disaster Analysis]", divider="grey")

with st.container(border=True):
    st.write(t.TEXT_INTRO)

st.link_button(
    "Access EM-DAT for download",
    url="https://public.emdat.be/",
    use_container_width=True)

# EM-DAT data
file_upload_em = st.file_uploader(
    "Upload your EM-DAT xlsx file...",
    type=['xlsx'])

if file_upload_em:
    st.session_state['data'] = u.get_data(file=file_upload_em)

if 'data' in st.session_state:
    st.success("EM-DAT file upload successful!")

# UN data
allow_un_upload = st.toggle("Enable additional upload UN population data", key="un_toggle")
if allow_un_upload:
    file_upload_un = st.file_uploader(
        "Upload your UN csv file...",
        type=['csv'])

    if file_upload_un:
        st.session_state['un_data'] = u.get_un_data(file=file_upload_un)

if 'un_data' in st.session_state:
    st.success("UN file upload successful!")

m.write_impressum()
