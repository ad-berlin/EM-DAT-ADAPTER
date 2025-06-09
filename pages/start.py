import streamlit as st

from text.text_info import TEXT_INTRO
from utils.utils import get_data, get_filtered_data
from text.text_info import TEXT_IMPRESSUM


st.header(":violet[EM-DAT: Visualising International Disaster]", divider="rainbow")

st.write(TEXT_INTRO)

file_upload = st.file_uploader(
    "*Upload your EM-DAT xlsx file...*",
    type=['xlsx'],
)
if file_upload:
    st.session_state['data'] = get_data(file=file_upload)

if 'data' in st.session_state:
    st.success("File upload successful!")

st.divider()
st.write(TEXT_IMPRESSUM)

