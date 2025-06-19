import pandas as pd
import streamlit as st
import numpy as np

from utils.variables import (YEAR_START, MONTH_START, DAY_START, YEAR_END, MONTH_END, DAY_END, COUNTRY, REGION,
                             SUBREGION, LOCATION, RIVER, NUM, DIS_NAT_TECH, DIS_SUBGROUP, DIS_TYPE, DIS_SUBTYPE, ORIGIN,
                             ASS_TYPES, AID, RECONSTRUCTION, RECONSTRUCTION_ADJ, INSURED, INSURED_ADJ, DAMAGE,
                             DAMAGE_ADJ, MAG, MAG_SCALE, DEATHS, INJURED, AFFECTED, HOMELESS)
from text.text_info import help_dict, TEXT_HELP

st.cache_data()
def get_data(file) -> pd.DataFrame:
    data = pd.read_excel(file, sheet_name=0)

    # data[DEATHS] = data[DEATHS].fillna(0)  # WARNING! But to be visible in scatter!
    # data[INJURED] = data[INJURED].fillna(0)  # WARNING! But to be visible in scatter!
    # data[AFFECTED] = data[AFFECTED].fillna(0)  # WARNING! But to be visible in scatter!

    # fill nan in dates to first of month and first of year, even if unknown
    data[YEAR_START] = data[YEAR_START].astype(int)
    data[MONTH_START] = data[MONTH_START].fillna(1).astype(int)  # WARNING!
    data[DAY_START] = data[DAY_START].fillna(1).astype(int)  # WARNING!
    data[YEAR_END] = data[YEAR_END].astype(int)
    data[MONTH_END] = data[MONTH_END].fillna(1).astype(int)  # WARNING!
    data[DAY_END] = data[DAY_END].fillna(1).astype(int)  # WARNING!

    add_col_start = "Start Date"
    data[add_col_start] = pd.to_datetime({
        'year': data[YEAR_START],
        'month': data[MONTH_START],
        'day': data[DAY_START]
    })

    add_col_end = "End Date"
    data[add_col_end] = pd.to_datetime({
        'year': data[YEAR_END],
        'month': data[MONTH_END],
        'day': data[DAY_END]
    })

    data.sort_values(by=[add_col_start, add_col_end])

    add_col_duration = "Duration of Disaster"
    data[add_col_duration] = (data[add_col_end] - data[add_col_start]).dt.days + 1
    data[add_col_duration] = np.where(data[add_col_duration] <= 0, np.nan, data[add_col_duration])

    return data


def get_filtered_data(start, end, location: list, dis_type: list, df: pd.DataFrame):
    data = "123"
    return data


def write_help(page_in_capitals) -> None:
    with st.expander(TEXT_HELP, icon=':material/info:'):
        st.markdown(help_dict.get(f'HELP_{page_in_capitals}'))


def remove_outliner(data: pd.DataFrame, q_low, q_high, parameter, target):
    for disaster_type in data[target].unique():
        mask = data[target] == disaster_type

        high = data.loc[mask][parameter].quantile(q_high)
        low = data.loc[mask][parameter].quantile(q_low)

        outliner_mask = (data[parameter] < low) | (data[parameter] > high)

        data.loc[mask & outliner_mask][parameter] = np.nan
    return data

def treat_text_column(data: pd.DataFrame, column: str):
    data[column] = data[column].astype(str)
    data[column] = (
        data[column]
        .str.replace(' | ', ', ')  # replace | with same separator
        .str.replace(' and ', ', ')  # replace and with same separator
        .str.replace(' + ', ', ')  # replace + with same separator
        .str.replace(' & ', ', ')  # replace & with same separator
        .str.replace('(', '')  # remove open round bracket
        .str.replace(')', '')  # remove close round bracket
        .str.replace('[', '')  # remove open square brackets (literal string)
        .str.replace(']', '')  # remove close square brackets (literal string)
        .str.replace(' ; ', ', ')
        .str.replace('; ', ', ')
        .str.replace(' ,', ',')
        .str.replace('_', ' ')
    )
    return data