import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from utils import constants as c
from utils import modules as m
from utils import ut as u
from text import text_info as t

if 'data' not in st.session_state:
    st.error(t.ERROR_DATA)

else:
    df = st.session_state['data'].copy()

    m.write_help(page_in_capitals='EXPLORE')

    start, end = m.write_time(data=df)
    df = df.loc[df[c.YEAR_START] >= start]  # for un data >= 1950
    df = df.loc[df[c.YEAR_START] <= end]

    with st.expander("Information about the columns"):
        for col in sorted(df.columns):
            st.write(f":blue[{col}]: {t.info_dict.get(col)}")

    target_y = st.selectbox(label="Choose target column for analysis (y-axis)",
                            options=df.columns,
                            placeholder=f"Choose target column for analysis",
                            key="target_y")

    target_x = st.selectbox(label="Choose target column for analysis (x-axis)",
                            options=df.columns,
                            placeholder=f"Choose target column for analysis",
                            key="target_x")

    color = st.selectbox(label="Choose column for color differentiation",
                         options=df.columns,
                         placeholder=f"Choose color column for analysis",
                         key="color")

    hover_list = st.multiselect(label="Choose columns for hover information",
                                options=df.columns,
                                placeholder="Choose columns for hover information")

    st.write("here comes a button/toggle to disable 'filling data gaps with 0'.")  # TODO
    st.write("here comes a selectbox to decide over the type of plot.")  # TODO

    go_button = st.button("start plotting", use_container_width=True)

    if go_button:
        target_scatter = px.scatter(
            u.build_scatter_data(df),
            x=target_x,
            y=target_y,
            color=color,
            hover_data=hover_list,
            title=f"{target_y} over {target_x} differentiated by {color} ({start} to {end})",
            subtitle="data gaps filled with 0 for visualisation")
        st.plotly_chart(target_scatter)
        st.write(f'''
        {target_x} (x-axis): {t.info_dict.get(target_x)}  
        {target_y} (y-axis): {t.info_dict.get(target_y)}  
        {color} (color-parameter): {t.info_dict.get(color)}
        ''')

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
