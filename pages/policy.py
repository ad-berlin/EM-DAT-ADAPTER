import streamlit as st
import pandas as pd

from utils import constants as c
from utils import modules as m
from utils import ut as u
from text import text_info as t

st.subheader(t.HEADER, divider="grey")

if 'data' not in st.session_state:
    st.error(t.ERROR_DATA)

else:
    df = st.session_state['data'].copy()
    un_ctr = u.get_m49_dict(file="data/UNSD.xlsx")

    frame = pd.DataFrame(df[c.COUNTRY].unique())
    frame.columns = [c.OPT_COUNTRY]
    frame[c.ADMIN_C] = frame[c.OPT_COUNTRY].map(lambda x: t.country_label_dict.get(x, x))
    frame[c.SOVEREIGN_C] = frame[c.ADMIN_C].map(lambda x: un_ctr.get(c.SOVEREIGN_C).get(x, "no UN member (2025)"))
    frame[c.UN_M49_C] = frame[c.ADMIN_C].map(lambda x: un_ctr.get(c.UN_M49_C).get(x, "not in M49 standard (2025)"))
    frame[c.OPT_SUBREGION] = frame[c.ADMIN_C].map(lambda x: un_ctr.get(c.OPT_SUBREGION).get(x, "not in M49 standard (2025)"))
    frame[c.GEOGRAPH_SR] = frame[c.ADMIN_C].map(lambda x: un_ctr.get(c.GEOGRAPH_SR).get(x, "no data"))
    frame[c.OPT_REGION] = frame[c.ADMIN_C].map(lambda x: un_ctr.get(c.OPT_REGION).get(x, "not in M49 standard (2025)"))
    frame[c.CONTINENT_R] = frame[c.ADMIN_C].map(lambda x: un_ctr.get(c.CONTINENT_R).get(x, "no data"))


    with st.container(border=True):
        st.write("""
        *Country*  
        The term "Country" is not as neutral as one could wish, which is why multiple definitions are available
        here.  
        :blue[EM-DAT Countries] - The dataset is not manipulated and the labels as given by the CRED are used. [1]  
        :blue[UN Sovereign Countries] - The dataset is reduced to the 193 states of the UN council from 2025. 
        Occupied territory or special administrative regions are attributed to the sovereign country. 
        [2][3]  
        :blue[Administrative Regions] - Regions which have special administrative status, are under occupation, or are overseas
        territory are separated from their main land to allow individual analysis. [3]  
        :blue[UN M49 Countries] - Countries are defined as in the most recent UN M49 standard. [4]
        """)
        with st.expander("Exact mapping of countries"):
            st.dataframe(frame[[c.OPT_COUNTRY, c.ADMIN_C, c.SOVEREIGN_C, c.UN_M49_C]], hide_index=True)

    with st.container(border=True):
        st.write("""
        *Subregion*  
        Based on "Countries" "Subregions" can be diverged. These are subjective groupings for broader pattern analysis.
        Two groupings are provided.  
        :blue[Geographical Subregions] - The aim is to group countries by shared geographical traits, locations, and/or water
        sources.
        :blue[UN M49 Subregions] - Subregions are defined as in the UN M49 standard. [4]
        """)
        with st.expander("Exact mapping of subregions"):
            st.dataframe(frame[[c.ADMIN_C, c.OPT_SUBREGION, c.GEOGRAPH_SR]], hide_index=True)

    with st.container(border=True):
        st.write("""
        *Region*  
        Based on "Subregions" "Regions" can be diverged. These are subjective groupings for broader pattern analysis.
        Two groupings are provided.  
        :blue[Continents] - The aim is to group countries by shared geographical traits, locations, and/or water
        sources.  
        :blue[UN M49 Regions] - Regions are defined as in the UN M49 standard. [4]
        """)
        with st.expander("Exact mapping of regions"):
            st.dataframe(frame[[c.ADMIN_C, c.OPT_REGION, c.CONTINENT_R]], hide_index=True)

    with st.container(border=True):
        st.write("""
        All of these definitions should support representation of human beings and their suffering through disasters.
        If important definitions are missing or active definitions are lacking or offending, please do not hesitate to
        inform the developer and provide data and/or sources to further improve this web tool.
        """)

m.write_impressum()
