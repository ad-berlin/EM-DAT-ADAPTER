import streamlit as st

from utils import constants as c
from utils import modules as m
from utils import ut as u
from text import text_info as t

st.subheader(":blue[DisTrack - International Disaster Analysis]", divider="grey")

with st.container(border=True):
    st.write(":blue[I want to give feedback...]")
    st.write('''
    Constructive feedback is very welcome! Please write an e-mail with your remarks to the following address:
    to_be_filled@something.com. If you find a bug or something that needs improving, please attach a screenshot. If
    something is missing, please try to describe it in detail or attach a sketch of what you would like to have on
    display.
    
    Not all feedback will be implemented.
    ''')

with st.container(border=True):
    st.write(":blue[I want to contribute to the code...]")
    st.write('''
    The code is open source and available via GitHub here (link). Please look through the existing code first and then
    request rights to push via GitHub and additionally write an e-mail to to_be_filled@something.com where you roughly
    describe the changes, that you propose.
    
    Not all proposals will be granted.
    ''')

with st.container(border=True):
    st.write(":blue[I have additional knowledge/data that should be displayed...]")
    st.write('''
    As displayed in the section about data quality, data is lacking in the database. If you know of open access
    databases that could be merged to show better picture of reality, this is very welcome.
    Please write an e-mail to to_be_filled@something.com, covering  
    - a link to the database,  
    - a short argument, why you thing this database is trustworthy with sources, and  
    - your background in research/interest.
    
    Please use your academic/official e-mail-address and maybe coordinate with your research group in what would be
    important for you.
    
    Depending on data quality and compatibility of the proposed database it is going to take time.
    ''')

with st.container(border=True):
    st.write(":blue[I want to advocate for better international data availability...]")
    st.write('''
    The main source of EM-DAT is the United Nations and insurance companies. But there is an immense gap in which
    countries and regions are covered and which are not. If you want to advocate ...
    ''')

st.divider()
st.write(t.TEXT_IMPRESSUM)