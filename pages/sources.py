import streamlit as st

from utils import modules as m
from text import text_info as t

st.subheader(t.HEADER, divider="grey")

with st.container(border=True):
    st.write("""
    :violet[Sources of the "About" page]  
    [1] https://emview.streamlit.app/ 
    """)

with st.container(border=True):
    st.write("""
    :violet[Sources of the "Start" page]  
    [1] https://www.emdat.be/  
    [2] https://public.emdat.be/
    """)

with st.container(border=True):
    st.write("""
    :violet[Sources of the "Definitions and Terminology" page]  
    [1] https://doc.emdat.be/docs/data-structure-and-content/spatial-information/  
    [2] https://www.un.org/en/about-us/member-states  
    [3] https://www.un.org/dppa/decolonization/en/nsgt  
    [4] https://unstats.un.org/unsd/methodology/m49/  
    """)

m.write_impressum()
