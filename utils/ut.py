import pandas as pd
import streamlit as st
import numpy as np
from unidecode import unidecode

from utils import constants as c
from text import text_info as t

@st.cache_data()
def get_m49_dict(file) -> dict:
    un_data_ctr = pd.read_excel(file)
    un_data_ctr = un_data_ctr.set_index("Country/Area")
    return un_data_ctr.to_dict()


@st.cache_data()
def get_un_data(file) -> pd.DataFrame:
    data = pd.read_csv(file)
    data = data[['LocID', 'Location', 'Time', 'TPopulation1Jan', 'PopDensity', 'MedianAgePop']]
    data = data.loc[data['LocID'] <= 900]
    return data


@st.cache_data()
def get_data(file) -> pd.DataFrame:
    un_ctr = get_m49_dict(file="data/UNSD.xlsx")
    un_pop = get_un_data(file="data/UN_DEMOGRAPH.csv")

    data = pd.read_excel(file, sheet_name=0)
    data = data.loc[data[c.DIS_NAT_TECH] == 'Natural']

    add_col_start = c.DATE_START
    data[add_col_start] = pd.to_datetime({
        'year': data[c.YEAR_START],
        'month': data[c.MONTH_START].fillna(1).astype(int),
        'day': data[c.DAY_START].fillna(1).astype(int)
    })

    add_col_end = c.DATE_END
    data[add_col_end] = pd.to_datetime({
        'year': data[c.YEAR_END],
        'month': data[c.MONTH_END].fillna(1).astype(int),
        'day': data[c.DAY_END].fillna(1).astype(int)
    })

    add_col_duration = c.DIS_DURATION
    data[add_col_duration] = (data[add_col_end] - data[add_col_start]).dt.days + 1
    data[add_col_duration] = np.where(data[add_col_duration] <= 0, np.nan, data[add_col_duration])

    add_col_origin_clean = c.ORIGIN_CLEAN
    data[add_col_origin_clean] = data[c.ORIGIN].map(lambda x: treat_origin(aim_list=t.spell_aim_list, string=x))

    add_col_origin_label = c.ORIGIN_LABEL
    data[add_col_origin_label] = data[add_col_origin_clean].map(lambda x: label_origin(string=x))

    add_col_admin = c.ADMIN_C
    data[add_col_admin] = data[c.COUNTRY].map(lambda x: t.country_label_dict.get(x, x))

    add_col_un_sov = c.SOVEREIGN_C
    data[add_col_un_sov] = data[add_col_admin].map(lambda x: un_ctr.get(add_col_un_sov).get(x, "no UN member (2025)"))

    add_col_un_m49_c = c.UN_M49_C
    data[add_col_un_m49_c] = data[add_col_admin].map(lambda x: un_ctr.get(add_col_un_m49_c).get(x, "not in M49 standard (2025)"))

    add_col_code_r = c.M49_CODE_R
    data[add_col_code_r] = data[add_col_admin].map(lambda x: un_ctr.get(add_col_code_r).get(x, 000)).astype(int)

    add_col_code_subr = c.M49_CODE_SR
    data[add_col_code_subr] = data[add_col_admin].map(lambda x: un_ctr.get(add_col_code_subr).get(x, 000)).astype(int)

    add_col_code_intr = c.M49_CODE_IR
    data[add_col_code_intr] = data[add_col_admin].map(lambda x: un_ctr.get(add_col_code_intr).get(x, 000)).astype(int)

    add_col_intr = c.UN_M49_IR
    data[add_col_intr] = data[add_col_admin].map(lambda x: un_ctr.get(add_col_intr).get(x, "no data"))

    add_col_code_c = c.M49_CODE_C
    data[add_col_code_c] = data[add_col_admin].map(lambda x: un_ctr.get(add_col_code_c).get(x, 000)).astype(int)

    add_col_code_isoa2 = c.ISO_A2
    data[add_col_code_isoa2] = data[add_col_admin].map(lambda x: un_ctr.get(add_col_code_isoa2).get(x, "no data"))

    add_col_code_isoa3 = c.ISO_A3
    data[add_col_code_isoa3] = data[add_col_admin].map(lambda x: un_ctr.get(add_col_code_isoa3).get(x, "no data"))

    add_col_geograph = c.GEOGRAPH_SR
    data[add_col_geograph] = data[add_col_admin].map(lambda x: un_ctr.get(add_col_geograph).get(x, "no data"))

    add_col_continent = c.CONTINENT_R
    data[add_col_continent] = data[add_col_admin].map(lambda x: un_ctr.get(add_col_continent).get(x, "no data"))

    return data


def remove_outliner(data: pd.DataFrame, q_low, q_high, parameter, target):
    for disaster_type in data[target].unique():
        mask = data[target] == disaster_type

        high = data.loc[mask][parameter].quantile(q_high)
        low = data.loc[mask][parameter].quantile(q_low)

        outliner_mask = (data[parameter] < low) | (data[parameter] > high)

        data.loc[mask & outliner_mask][parameter] = np.nan
    return data


def treat_text_column(data: pd.DataFrame, columns: list, new=False):
    for column in columns:
        if new:
            column_new = f"{column} (assist)"
        else:
            column_new = column

        data[column_new] = data[column].astype(str)
        data[column_new] = data[column_new].str.lower().apply(unidecode)
        data[column_new] = (
            data[column_new]
            .str.replace('"', '')
            .str.replace("'", '')

            .str.replace(';', ',')
            .str.replace('.', ',')
            .str.replace('|', ',')
            .str.replace('[', '(')
            .str.replace(']', ')')
            .str.replace('&', ' and ')
            .str.replace('+', ' and ')

            .str.replace('_', ' ')
            .str.replace('  ', ' ')

            .str.replace(' ,', ',')
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
    new_data = data.copy()
    for col in c.int_list:
        new_data[col] = new_data[col].fillna(0)
    return new_data


def treat_origin(aim_list: list, string):
    if not isinstance(string, str):
        return "no data"

    replacement = ""

    work_string = string.lower()
    work_string = (work_string
                   .replace(',', replacement)
                   .replace(';', replacement)
                   .replace('+', replacement)
                   .replace('.', replacement)
                   .replace('"', replacement)
                   .replace("'", replacement)

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


def ready_to_filter(data: pd.DataFrame):
    columns = [c.RIVER, c.LOCATION, c.ASS_TYPES]
    data = treat_text_column(data=data, columns=columns, new=True)
    return data
