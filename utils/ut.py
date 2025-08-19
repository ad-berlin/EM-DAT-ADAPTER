import pandas as pd
import streamlit as st
import numpy as np

from utils import constants as c
from text import text_info as t
from text import countries as ctr


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

    add_col_un_m49_c = 'UN M49 Countries'  # ?? distinction to EM-DAT?
    data[add_col_un_m49_c] = 'Country'

    add_col_admin = 'Administrative Regions'
    data[add_col_admin] = data[c.COUNTRY].map(lambda x: ctr.country_label_dict.get(x, x))

    add_col_un_sov = 'UN Sovereign Countries'
    data[add_col_un_sov] = data[c.COUNTRY].map(lambda x: ctr.non_self_gov_2025_dict.get(x, x))
    data[add_col_un_sov] = data[add_col_un_sov].map(lambda x: ctr.overseas_terr_dict.get(x, x))
    data[add_col_un_sov] = data[add_col_un_sov].map(lambda x: ctr.country_local_name_un_2025_dict.get(x, "not sovereign (UN 2025)"))

    add_col_un_m49_subr = 'UN M49 Subregions'  # probably == SUBREGIONS
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
    # TODO: replace empty/space/"nan" to "no data"
    return data


def build_scatter_data(data: pd.DataFrame):
    for col in c.int_list:
        data[col] = data[col].fillna(0)
    return data


def treat_origin(aim_list: list, string):
    if not isinstance(string, str):
        return "no data"

    replacement = ""

    work_string = string.lower()
    work_string = (work_string
                   .replace(',', replacement)
                   .replace(';', replacement)
                   .replace(' +', replacement)
                   .replace('.', replacement)
                   .replace('"', replacement)
                   .replace(' of', "_of")
                   .replace(' with', "_with")
                   )

    word_list = work_string.split(' ')

    new_word_list = []
    for word in word_list:
        new_word = treat_origin_word(aim_list=aim_list, test=word)
        new_word = t.word_origin_map.get(new_word, new_word)
        new_word_list.append(new_word)

    new_string = ' '.join(new_word_list)

    new_string = (new_string
                  .replace('_of', ' of')
                  .replace('_with', " with")
                  .replace('  ', ' ')
                  )

    return new_string


def treat_origin_word(aim_list, test):

    argument_list = [test, test[0:-1], test[0:-2]]  # check for similar writing e.g. rain, rains; monsoon, monsoonal
    for argument in argument_list:
        if argument in aim_list:
            return argument

    len_test = len(test)  # save length of test word
    count_test = {}  # build dict with alphabetic counting of letters for test word
    for x in sorted(set(test)):
        count_test.update({x: list(test).count(x)})

    for aim in aim_list:
        len_aim = len(aim)  # save length of aim word
        count_aim = {}  # build dict with alphabetic counting of letters for aim word
        for x in sorted(set(aim)):
            count_aim.update({x: list(aim).count(x)})

        smooth_num = 0
        if count_test == count_aim:  # when exact same letters are used (comparison anagram)
            smooth_num += len_aim * 0.6
        if len_aim <= 5:  # short words e.g. rain, heavy
            smooth_num += 1
        elif len_aim <= 8:  # medium words e.g. monsoon, rainfall, snowmelt
            smooth_num += 2
        else:  # longer words e.g. lightning, torrential
            smooth_num += 3

        if abs(len_aim - len_test) >= 3:  # setting boundaries in differing length
            continue
        else:
            distance = levenshtein_distance(s1=test, s2=aim)
            if distance <= smooth_num:
                return aim

    return test


def levenshtein_distance(s1: str, s2: str) -> int:
    len_s1, len_s2 = len(s1), len(s2)

    dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

    for i in range(len_s1 + 1):
        dp[i][0] = i
    for j in range(len_s2 + 1):
        dp[0][j] = j

    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost)

    return dp[len_s1][len_s2]


def label_origin(string):
    new_string = []
    for word in t.one_word_descriptor_lst:
        if word in string:
            new_string.append(word)
    for duo in t.two_word_descriptor_lst:
        label = t.mapping_origin_labels.get(duo[0])
        if duo[0] in string and duo[1] in string:
            new_string.append(label)
    for comp in t.complex_label_lst:
        label = t.mapping_origin_labels.get(comp[0])
        for word in comp:
            if word in string:
                new_string.append(label)
    for descr in t.rain_descriptor_lst:
        label = t.mapping_origin_labels.get(descr)
        if f"{descr} rain" in string:
            new_string.append(label)
    if "snow" in string and "melt" not in string:
        new_string.append(t.mapping_origin_labels.get("snow"))
    if not new_string:
        new_string.append(t.mapping_origin_labels.get("unclear"))
    return '; '.join(set(new_string))