import streamlit as st
import plotly.express as px
import pandas as pd

from utils import constants as c
from text.text_info import TEXT_IMPRESSUM, error_dict, select_dict, month_dict
from utils.ut import write_help, treat_text_column, build_scatter_data
if 'data' not in st.session_state:
    st.error(error_dict.get('ERROR_DATA'))

else:
    df = st.session_state['data'].copy()

    write_help(page_in_capitals='EXPLORE')


    def misspelling(aim_list, string, treat_and_as_separator=False):
        string = string.lower()
        string = (string.replace(', ', ' ')
                  .replace('; ', ' '))

        if treat_and_as_separator:
            string = string.replace(' and ', ' ')

        string_list = string.split(' ')

        new_string_list = []
        for word in string_list:
            if len(word) > 7:
                new_word = treat_word(aim_list=aim_list, test=word, smooth_num=2)
                new_string_list.append(new_word)
            else:
                new_word = treat_word(aim_list=aim_list, test=word, smooth_num=1)
                new_string_list.append(new_word)
        return f"{' '.join(new_string_list)}"


    def treat_word(aim_list, test, smooth_num):
        aim_short_list = []
        aim_len_list = [(aim, len(aim)) for aim in aim_list]
        for ix in range(len(aim_len_list)):
            if aim_len_list[ix][1] - smooth_num <= len(test) <= aim_len_list[ix][1] + smooth_num:
                aim_short_list.append(aim_len_list[ix][0])

        for aim in aim_short_list:
            set_aim = sorted(set(aim))
            set_test = sorted(set(test))

            count_aim = []
            for letter in set_aim:
                count = list(aim).count(letter)
                count_aim.append(count)

            count_test = []
            for letter in set_aim:
                count = list(test).count(letter)
                count_test.append(count)

            diff_list_aim = []
            for ix in range(len(set_aim)):
                diff = abs(count_test[ix] - count_aim[ix])  # TODO: fix
                diff_list_aim.append(diff)

            diff_list_test = []
            for ix in range(len(set_test)):
                diff = abs(count_aim[ix] - count_test[ix])  # TODO: fix
                diff_list_test.append(diff)

            if sum(diff_list_aim) <= smooth_num and sum(diff_list_test) <= smooth_num:
                return f"{aim}({test})"
        else:
            return test


    spell_aim_list = ["rainfall", "monsoon", "heavy", "lightning", "torrential", "insufficient", "thunderstorm", "continuous", "wind", "precipitation"]
    # DOES NOT WORK: seasonal (associated), continuous (consumption), rain (air, rapid, much more!), wind (dawn), monsoon (anomalous, continous, non-stop, [mousson])
    # df[c.ORIGIN] = df[c.ORIGIN].map(lambda x: misspelling(aim_list=spell_aim_list, string=f"{x}", treat_and_as_separator=True))
    # df[c.ORIGIN] = df[c.ORIGIN].str.split(" ")  # interesting
    # st.write(df[c.ORIGIN].value_counts())

    # info = f'{' '.join(df[c.ORIGIN].astype(str))}'
    # info = pd.Series(info.split(' ')).value_counts()
    # st.write(info)



with st.container(border=True):
    st.write('test123')
    with st.container(border=True):
        with st.container(border=True):
            st.write("test123")
            with st.container(border=True):
                st.write("test123")
                col1, col2, col3 = st.columns(3)
                with col1.container(border=True):
                    st.write("test123")
                with col2.container(border=True):
                    st.write("test123")
                with col3.container(border=True):
                    st.write("test123")

# argument_list = [word, word[0:-1], word[0:-2]]
# for argument in argument_list:
#     if argument in aim_list:
#         new_string_list.append(argument)
#         break

st.divider()
st.write(TEXT_IMPRESSUM)
