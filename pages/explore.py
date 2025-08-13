import streamlit as st
import numpy as np
import pandas as pd

from utils import constants as c
from utils import modules as m
from utils import ut as u
from text import text_info as t


if 'data' not in st.session_state:
    st.error(t.ERROR_DATA)

else:
    df = st.session_state['data'].copy()

    m.write_help(page_in_capitals='EXPLORE')


    def misspelling(aim_list: list, string, treat_and_as_separator=False):
        if not isinstance(string, str):
            return "no data"

        separator = " |"

        string = string.lower()
        string = (string
                  .replace(',', separator)
                  .replace(';', separator)
                  .replace(' +', separator)
                  .replace('.', '')
                  .replace('  ', ' ')
                  .replace('"', "'")
                  .replace(' of', "_of")
                  )

        if treat_and_as_separator:
            string = string.replace(' and ', ' | ')

        word_list = string.split(' ')

        new_word_list = []
        for word in word_list:
            new_word = treat_word(aim_list=aim_list, test=word)
            new_word = word_map.get(new_word, new_word)
            new_word_list.append(new_word)

        new_string = ' '.join(new_word_list)
        new_string = new_string.replace('_of', ' of')

        return new_string


    def treat_word(aim_list, test):

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
                smooth_num += len_aim - 2
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


    spell_aim_list = ["rain", "heavy", "rainfall", "rains", "snowmelt", "monsoon", "monsoonal", "lightning", "torrential",
                      "temperature", "thunderstorm", "continuous", "wind", "precipitation", "storm"]
    main_label = ["rain", "monsoon", "melting snow", "storm", "tropical depression", "thunderstorm/lightning",
                  "el nino", "la nina", "typhoon", "drought/insufficient rain", "wind", "high temperatures", "tropical depression",
                  "cyclone", "dry conditions", "hurricane", "mei-yu", "sanitation/hygiene", "drinking water", "cold front",
                  "dam/levy break/release"]
    descriptors = ["extreme", "fast", "unseasonal", "continuous", "insufficient", "short"]

    word_map = {
        # synonyms main label
        "rainfall": "rain",
        "rains": "rain",
        "precipitation": "rain",
        "snowfall": "snow",
        "monsoonal": "monsoon",
        "snowmelt": "melting snow",  # contains "snow" and "melt"
        # "heat": "high temperatures",  # heat wave
        # category synonyms "extreme"
        "heavy": "extreme",
        "excessive": "extreme",
        "intense": "extreme",
        "severe": "extreme",
        "strong": "extreme",
        "violent": "extreme",
        "massive": "extreme",
        # category synonyms "continuous"
        "non-stop": "continuous",
        "incessant": "continuous",
        "prolonged": "continuous",
        "long-term": "continuous",
        "uninterrupted": "continuous",
        "ongoing": "continuous",
        "long-lasting": "continuous",
        "persistent": "continuous",
        "days_of": "continuous",
        "constant": "continuous",
        # category synonyms "irregular"
        "erratic": "irregular",
        # category synonyms "insufficient"
        "poor": "insufficient",
        "limited": "insufficient",
        "below-average": "insufficient",
        "reduced": "insufficient",
        # "low": "insufficient",  # bec. combination with temperature
        "scarcity_of": "insufficient",
        "lack_of": "insufficient",
        # category synonyms "rapid", "fast", "sudden"
    }

    ### if structure as follows: | descriptor1 AND descriptor2 S:label S:note |
    ### resulting structure should be descriptor1 sum[label] (sum[note]) | descriptor2 sum[label] (sum[note])
    ### if pre and post AND num of label > num of descriptor AND = |

    ### idea for future processing: setting options in descriptors and labels and then allowing only selection or note
    ### new labels can be introduced by admin

    # st.write(treat_word(aim_list=["continuous"], test="conditions", smooth_num=2))
    # st.write(levenshtein_distance(s1="rain", s2="rain"))

    add_new_col = "origin new col"
    df[add_new_col] = df[c.ORIGIN].map(lambda x: misspelling(aim_list=spell_aim_list, string=x, treat_and_as_separator=True))

    df_test = df.loc[df[add_new_col].str.contains("storm")]
    st.write(df_test[[c.ORIGIN, add_new_col]])

    # info = f'{' | '.join(df[c.ORIGIN].astype(str))}'
    # info = pd.Series(info.split(' | ')).value_counts()
    # st.write(info)

st.divider()
st.write(t.TEXT_IMPRESSUM)
