import streamlit as st

from text import text_info as t
from utils import modules as m

st.subheader(":blue[DisTrack - International Disaster Analysis]", divider="grey")

st.write(t.TEXT_ABOUT)

with st.expander("List of contributors"):
    st.write("List of contributors...")

st.write(":violet[You want to contribute as well? Find out how to participate!]")

m.write_impressum()
