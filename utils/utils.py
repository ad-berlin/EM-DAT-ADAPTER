import pandas as pd
import streamlit as st
import numpy as np

from text.countries import country_label_dict, non_self_gov_2025_dict, country_local_name_un_2025_dict, \
    overseas_terr_dict
from utils.variables import (YEAR_START, MONTH_START, DAY_START, YEAR_END, MONTH_END, DAY_END, COUNTRY, REGION,
                             SUBREGION, LOCATION, RIVER, NUM, DIS_NAT_TECH, DIS_SUBGROUP, DIS_TYPE, DIS_SUBTYPE, ORIGIN,
                             ASS_TYPES, AID, RECONSTRUCTION, RECONSTRUCTION_ADJ, INSURED, INSURED_ADJ, DAMAGE,
                             DAMAGE_ADJ, MAG, MAG_SCALE, DEATHS, INJURED, AFFECTED, HOMELESS)
from text.text_info import help_dict, TEXT_HELP

st.cache_data()
def get_data(file) -> pd.DataFrame:
    data = pd.read_excel(file, sheet_name=0)

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

    add_col_un_m49_c = 'UN M49 Countries'  # ?? unterschied zu EM-DAT?
    data[add_col_un_m49_c] = 'Country'

    add_col_admin = 'Administrative Regions'
    data[add_col_admin] = data[COUNTRY].map(lambda x: country_label_dict.get(x, x))

    add_col_un_sov = 'UN Sovereign Countries'
    data[add_col_un_sov] = data[COUNTRY].map(lambda x: non_self_gov_2025_dict.get(x, x))
    data[add_col_un_sov] = data[add_col_un_sov].map(lambda x: overseas_terr_dict.get(x, x))
    data[add_col_un_sov] = data[add_col_un_sov].map(lambda x: country_local_name_un_2025_dict.get(x, "not sovereign (UN 2025)"))

    add_col_un_m49_subr = 'UN M49 Subregions'  # vmtl. == SUBREGIONS
    data[add_col_un_m49_subr] = 'Subregion'

    add_col_geograph = 'Geographical Regions'
    data[add_col_geograph] = 'Region'

    add_col_un_m49_r = 'UN M49 Regions'  # vmtl. == REGIONS
    data[add_col_un_m49_r] = 'Region'

    add_col_continent = 'Continents'
    data[add_col_continent] = 'Continent'

    return data


st.cache_data()
def get_un_data(file) -> pd.DataFrame:
    data = pd.read_csv(file)
    data = data[['SortOrder', 'LocID', 'Location', 'Time', 'TPopulation1Jan', 'PopDensity', 'MedianAgePop']]
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
    data[column] = data[column].str.lower()
    data[column] = (
        data[column]
        .str.replace('|', ',')
        .str.replace('(1)', '')
        .str.replace('(2)', '')
        .str.replace('(3)', '')
        .str.replace('(4)', '')
        .str.replace('+', ',')
        .str.replace(' - ', ',')
        .str.replace('&', ',')
        .str.replace('[', '(')
        .str.replace(']', ')')
        .str.replace(';', ',')
        .str.replace('_', ' ')
        .str.replace(' ,', ',')
        .str.replace(', ', ',')
        .str.replace(',', ', ')
    )
    # ISSUES
    # further information can be provided in brackets e.g. Couronnes station (Paris); Gainesville (Georgia)
    # further information can be provided after comma e.g. Roger's Pass, British Columbia; Spanish River, Ontario
    # further information can be provided after dash e.g. Aomori Prefecture - Hokkaido
    # unspecific locations e.g. North; Western; South; Small Island between Java and Sumatra; Central, South-West
    # meaning all country: Countrywide; Nationwide; All country; Much of nation
    # wierd additional means e.g. Honshu + other Isles; Belize city other towns
    # &, +, ;, |, instead of ,
    # listings in brackets are possible e.g. Kanto plaine (Yokohama,Tokyo)
    # appearence of numbering e.g. (1) Weluwun Qtr, Rangoon, (2) W. Okkyin Qtr, Rangoon, (3) Palaing Qtr, Mandalay
    # two optional writings e.g. Sichuan/Chongqing airport; Valle d'Aosta/Vallée d'Aoste
    return data