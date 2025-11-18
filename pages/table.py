import pandas as pd
import streamlit as st

from utils import constants as c
from utils import modules as m
from utils import ut as u
from text import text_info as t
from utils.constants import regions_list

st.subheader(t.HEADER, divider="grey")

if 'data' not in st.session_state:
    st.error(t.ERROR_DATA)

else:
    df = st.session_state['data'].copy()

    m.write_help(page_in_capitals='TABLE')

    with st.container(border=True):
        st.write(f":blue[I have the {c.NUM} and want to see the full dataset]")
        dis_no = st.text_input(label=f"{c.NUM} input",
                               label_visibility="collapsed",
                               placeholder=f"Please type the {c.NUM}")
        if dis_no:
            st.dataframe(df.loc[df[c.NUM] == dis_no], hide_index=True)

    with st.container(border=True):
        st.write(":blue[I want to filter certain parameters, ...]")
        info = []
        filter_params = st.multiselect(label="params for filter",
                                       options=sorted(c.filter_list),
                                       label_visibility="collapsed",
                                       placeholder="Choose parameters for filter options")
        for param in filter_params:
            st.write(f"Filter {param}")
            df[c.text_field_list] = df[c.text_field_list].fillna(value="no data")

            # a slider for floats
            if param in c.int_list or param in c.date_list:
                min_val, max_val = st.select_slider(label=f"{param} to filter",
                                                    options=sorted(df[param].fillna(df[param].min()).unique()),
                                                    value=(df[param].min(), df[param].max()),
                                                    label_visibility="collapsed")
                df = df.loc[df[c.YEAR_START] >= min_val]
                df = df.loc[df[c.YEAR_START] <= max_val]
                info.append((param, f"{min_val} - {max_val}"))

            # text input field
            elif param in c.text_field_list:
                argument = st.text_input(label=f"{param} to filter",
                                         label_visibility="collapsed",
                                         placeholder="Please type what you look for")
                df = df.loc[df[param].str.contains(argument)]
                info.append((param, [argument]))

            else:
                argument = st.multiselect(label=f"{param} to filter",
                                          options=df[param].unique(),
                                          label_visibility="collapsed")
                pattern = "|".join(argument)
                df = df[df[param].str.contains(pattern, na=False)]  # na=False: treat NaN as False
                info.append((param, argument))

        st.write(":blue[...see the table, ...]")
        st.dataframe(df, hide_index=True)

        info = pd.DataFrame(info)
        download = st.button(":blue[...and save as ExcelFile.]", use_container_width=True)
        if download:
            with pd.ExcelWriter("DisTrack_filtered.xlsx") as writer:
                df.to_excel(writer, sheet_name="filtered_data", index=False)
                info.to_excel(writer, sheet_name="filter_info")

m.write_impressum()
