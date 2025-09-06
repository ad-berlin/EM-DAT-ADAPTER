import streamlit as st

from utils import modules as m
from utils import ut as u
from text import text_info as t

st.subheader(t.HEADER, divider="grey")

with st.container(border=True):
    st.write(t.TEXT_INTRO)

st.link_button(
    "access EM-DAT for download",
    url="https://public.emdat.be/",
    use_container_width=True)

# EM-DAT data
file_upload_em = st.file_uploader(
    "Upload here your EM-DAT xlsx file!",
    type=['xlsx'])

if file_upload_em:
    st.session_state['data'] = u.get_data(file=file_upload_em)

if 'data' in st.session_state:
    st.success("File upload successful!")


m.write_impressum()
