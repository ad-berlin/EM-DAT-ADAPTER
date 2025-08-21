import streamlit as st
import pandas as pd
import numpy as np

from utils import constants as c
from utils import modules as m
from utils import ut as u
from text import text_info as t


if 'data' not in st.session_state:
    st.error(t.ERROR_DATA)

else:
    df = st.session_state['data'].copy()

    m.write_help(page_in_capitals='EXPLORE')

    add_col_un_m49_c = c.UN_M49_C
    # data[add_col_un_m49_c] = 'Country'

    add_col_un_sov = c.SOVEREIGN_C
    # data[add_col_un_sov] = data[c.COUNTRY].map(lambda x: ctr.non_self_gov_2025_dict.get(x, x))
    # data[add_col_un_sov] = data[add_col_un_sov].map(lambda x: ctr.overseas_terr_dict.get(x, x))
    # data[add_col_un_sov] = data[add_col_un_sov].map(lambda x: ctr.country_local_name_un_2025_dict.get(x, "not sovereign (UN 2025)"))


    st.write(df)


    # df_test = df.loc[df[add_new_col].str.contains(" test 123 ")]
    # df_test = df.loc[df[add_col_origin_label].str.contains(" test 123 ")]
    # df_test = df_test.loc[df_test[add_col_origin_label] != "no data"]

    # st.write(df_test[add_col_origin_label].value_counts())
    # st.write(df_test[[c.ORIGIN, add_col_origin_clean, add_col_origin_label]])

    # info = f'{' | '.join(df[add_col_origin_label].astype(str))}'
    # info = pd.Series(info.split(' | ')).value_counts()
    # st.write(info)

m.write_impressum()
