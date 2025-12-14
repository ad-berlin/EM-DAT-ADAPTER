import streamlit as st

from utils import modules as m
from utils import ut as u
from text import text_info as t
from utils import constants as c

st.subheader(t.HEADER, divider="grey")

m.write_help(page_in_capitals='START')

with st.container(border=True):
    st.success("""
    Dear Beta-User, you have two main tasks:  
    1) Please, find a way to create graphs that are most useful for your field of research.  
    2) Please, try to break the app.
    
    Most gratefully,  
    The Developer
    """)

    st.link_button(
        ":red[please document your results as good as possible here in this survey]",
        url="https://diazberlin.limesurvey.net/distrack_beta_eval?lang=en&newtest=Y",
        use_container_width=True)

with st.container(border=True):
    st.write(t.TEXT_INTRO)

st.link_button(
    "access EM-DAT for download",
    url="https://public.emdat.be/",
    use_container_width=True)

# EM-DAT data
file_upload_em = st.file_uploader(
    ":blue[Upload here your EM-DAT xlsx file!]",
    type=['xlsx'])

if file_upload_em:
    st.session_state['data'] = u.get_data(file=file_upload_em)

if 'data' in st.session_state:
    st.success("File upload successful!")

m.write_impressum()
