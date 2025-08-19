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

    add_col_origin_clean = "Origin (clean)"
    df[add_col_origin_clean] = df[c.ORIGIN].map(lambda x: u.treat_origin(aim_list=t.spell_aim_list, string=x))

    add_col_origin_label = "Origin (label)"
    df[add_col_origin_label] = df[add_col_origin_clean].map(lambda x: u.label_origin(string=x))

    # df_test = df.loc[df[add_new_col].str.contains(" test 123 ")]
    # df_test = df.loc[df[add_col_origin_label].str.contains(" test 123 ")]
    # df_test = df_test.loc[df_test[add_col_origin_label] != "no data"]


    # st.write(df_test[add_col_origin_label].value_counts())
    # st.write(df_test[[c.ORIGIN, add_col_origin_clean, add_col_origin_label]])

    # info = f'{' | '.join(df[add_col_origin_label].astype(str))}'
    # info = pd.Series(info.split(' | ')).value_counts()
    # st.write(info)

m.write_impressum()
