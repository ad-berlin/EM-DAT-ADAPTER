import streamlit as st
from text.text_info import TEXT_IMPRESSUM

with st.container(border=True):
    st.write(":blue[General sources regarding EM-DAT and the 'Start' page...]")
with st.container(border=True):
    st.write(":blue[Specific sources regarding the 'Per classification' page...]")
with st.container(border=True):
    st.write(":blue[Specific sources regarding the 'Per region' page...]")
with st.container(border=True):
    st.write(":blue[Additional sources regarding definitions and data biases...]")

st.divider()
st.write(TEXT_IMPRESSUM)