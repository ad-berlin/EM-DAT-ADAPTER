import streamlit as st

from utils import constants as c
from utils import modules as m
from utils import ut as u
from text import text_info as t

with st.container(border=True):
    st.write(":blue[General sources regarding EM-DAT and the 'Start' page]")
with st.container(border=True):
    st.write(":blue[Specific sources regarding the 'Per Classification' page]")
with st.container(border=True):
    st.write(":blue[Specific sources regarding the 'Per Region' page]")
with st.container(border=True):
    st.write(":blue[Additional sources regarding definitions and data biases]")

m.write_impressum()
