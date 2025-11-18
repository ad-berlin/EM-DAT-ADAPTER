import streamlit as st

from text import text_info as t
from utils import modules as m

st.subheader(t.HEADER, divider="grey")

st.write(t.TEXT_ABOUT)

with st.expander("List of contributors"):
    st.write("List of contributors here to come...")

st.write(":violet[You want to contribute as well? Find out how to participate!]")

m.write_impressum()
