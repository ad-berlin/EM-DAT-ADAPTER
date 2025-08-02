import pandas as pd
import streamlit as st
import numpy as np

from utils import constants as c
from text.countries import country_label_dict, non_self_gov_2025_dict, country_local_name_un_2025_dict, \
    overseas_terr_dict
from text.text_info import help_dict, TEXT_HELP

st.cache_data()
def get_data(file) -> pd.DataFrame:
    data = pd.read_excel(file, sheet_name=0)
    data = data.loc[data[c.DIS_NAT_TECH] == 'Natural']

    # fill nan in dates to first of month and first of year, even if unknown
    data[c.YEAR_START] = data[c.YEAR_START].astype(int)
    data[c.MONTH_START] = data[c.MONTH_START].fillna(1).astype(int)  # WARNING!
    data[c.DAY_START] = data[c.DAY_START].fillna(1).astype(int)  # WARNING!
    data[c.YEAR_END] = data[c.YEAR_END].astype(int)
    data[c.MONTH_END] = data[c.MONTH_END].fillna(1).astype(int)  # WARNING!
    data[c.DAY_END] = data[c.DAY_END].fillna(1).astype(int)  # WARNING!

    add_col_start = "Start Date"
    data[add_col_start] = pd.to_datetime({
        'year': data[c.YEAR_START],
        'month': data[c.MONTH_START],
        'day': data[c.DAY_START]
    })

    add_col_end = "End Date"
    data[add_col_end] = pd.to_datetime({
        'year': data[c.YEAR_END],
        'month': data[c.MONTH_END],
        'day': data[c.DAY_END]
    })

    data.sort_values(by=[add_col_start, add_col_end])

    add_col_duration = "Duration of Disaster"
    data[add_col_duration] = (data[add_col_end] - data[add_col_start]).dt.days + 1
    data[add_col_duration] = np.where(data[add_col_duration] <= 0, np.nan, data[add_col_duration])

    add_col_un_m49_c = 'UN M49 Countries'  # ?? unterschied zu EM-DAT?
    data[add_col_un_m49_c] = 'Country'

    add_col_admin = 'Administrative Regions'
    data[add_col_admin] = data[c.COUNTRY].map(lambda x: country_label_dict.get(x, x))

    add_col_un_sov = 'UN Sovereign Countries'
    data[add_col_un_sov] = data[c.COUNTRY].map(lambda x: non_self_gov_2025_dict.get(x, x))
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
    # TODO: fix that stuff in brackets separated by comma stays together (maybe delete?)
    # TODO: replace empty/space/"nan" to np.nan
    return data

def treat_origin():
    # for misspellings:
    # len(word) == 4,5,6 and 4 letters are h, e, a, v, y --> heavy
    # len(word) == 3,4,5,6 and 3 letters are r, a, i, n, s --> rain
    # --> torrential (torrentila)
    # --> monsoonal
    # --> melting
    # --> lightning
    # --> poor, insufficient
    # --> of
    # --> seasonal
    # --> supply

    # poor, limited, insufficient
    # excessive, erratic, severe, strong, extreme, intense, heavy
    # rainfall(s), rain(s), raining, showers, rain
    # snowfall(s), snow fall(s)
    # snowmelt, snow melt, melting of snow, melting snow
    # non-stop, prolonged, long-term, uninterrupted, persistent, continuous

    # tremor == thunderstorm(s) ??
    # unseasonal ??

    a = 1
    return a


def build_scatter_data(data: pd.DataFrame):
    for col in c.int_list:
        data[col] = data[col].fillna(0)
    return data