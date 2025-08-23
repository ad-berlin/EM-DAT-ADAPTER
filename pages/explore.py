import streamlit as st
import pandas as pd
import numpy as np

from utils import constants as c
from utils import modules as m
from utils import ut as u
from text import text_info as t
from utils.ut import treat_text_column

if 'data' not in st.session_state:
    st.error(t.ERROR_DATA)

else:
    df = st.session_state['data'].copy()

    m.write_help(page_in_capitals='EXPLORE')

    start, end = m.write_time(data=df)
    df = df.loc[df[c.YEAR_START] >= start]  # for un data >= 1950
    df = df.loc[df[c.YEAR_START] <= end]


    # df_test = df.loc[df[add_col_origin_label].str.contains(" test 123 ")]
    # df_test = df_test.loc[df_test[add_col_origin_label] != "no data"]
    # st.write(df_test[c.LOCATION].value_counts())

    ### LOCATION TREAT as far as possible
    # treat_text_column(data=df, column=c.LOCATION)
    # df_test = df.loc[df[c.LOCATION].str.contains("no data")]
    # st.write(df_test[[c.DIS_SUBTYPE, c.LOCATION, c.ADMIN_C]])
    #
    # info = f'{', '.join(df[c.LOCATION].astype(str))}'
    # info = pd.Series(info.split(', ')).value_counts()
    # # for ix in info.index:
    # #     if "-" in ix:  # ":", "?", "/", "=", "-", ">", "_", ### not in string so far: !, %, §, [, ], |
    # #         st.write(ix)
    # st.write(info)

m.write_impressum()

### AREA ANALYSIS
# un_df = u.get_un_data(file="data/UN_DEMOGRAPH.csv")
# # un_df = un_df.loc[un_df['Time'] >= start]
# # un_df = un_df.loc[un_df['Time'] <= end]
# un_df = un_df.loc[un_df['LocID'] <= 900]
#
# m49_df = pd.read_excel("data/UNSD.xlsx")
# m49_df_dict = m49_df.set_index("Country/Area")
# m49_df_dict = m49_df_dict.to_dict()
#
#
# add_un_area = "CountryArea[km²]"
# un_df[add_un_area] = (un_df["TPopulation1Jan"] / un_df["PopDensity"]) * 1000

# un_ctr = sorted(un_df['LocID'].unique())
# admin_ctr = sorted(m49_df[c.M49_CODE_C].unique())
#
# for country in un_ctr:
#     if country not in admin_ctr and country != 900:
#         st.write(country)
#
# not_in_un_lst = []
# for country in admin_ctr:
#     if country not in un_ctr:
#         not_in_un_lst.append(country)
#
# for num in not_in_un_lst:
#     st.write(m49_df_dict.get("Country/Area").get(num, "ERROR"))

### TODO: implement analysis per km²
# area_dict = {}
# for country in sorted(df[c.ADMIN_C].unique()):
#     country_code = m49_df_dict.get(c.M49_CODE_C).get(country)
#     area = un_df.loc[un_df["LocID"] == country_code][add_un_area].mean()
#     area_dict.update({country: area})
# st.write(area_dict)