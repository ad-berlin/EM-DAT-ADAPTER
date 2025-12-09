import streamlit as st
import plotly.express as px

from utils import constants as c
from utils import modules as m
from utils import ut as u
from text import text_info as t

st.subheader(t.HEADER, divider="grey")


if 'data' not in st.session_state:
    st.error(t.ERROR_DATA)

else:
    if 'disable_color' not in st.session_state:
        st.session_state['disable_color'] = True
    if 'time_as_x' not in st.session_state:
        st.session_state['time_as_x'] = True
    if 'disable_hover' not in st.session_state:
        st.session_state['disable_hover'] = True

    color = c.HIST
    hover_list = []
    layout = [2,1]

    df = st.session_state['data'].copy()

    m.write_help(page_in_capitals='EXPLORE')

    with st.container(border=True):
        st.write(":blue[Build your own custom plot]")

        with st.expander("Information about the columns"):
            for col in sorted(df.columns):
                st.write(f":blue[{col}]: {t.info_dict.get(col)}")

        with st.container(border=True):
            st.write(":blue[Filter the data prior to plotting]")
            df, info_table = m.build_filter(data=df)

        target_y = st.selectbox(label="Choose target column for analysis (y-axis)",
                                options=df.columns,
                                placeholder=f"Choose target column for analysis",
                                key="target_y")

        col1, col2 = st.columns(layout)

        target_x = col1.selectbox(label="Choose target column for analysis (x-axis)",
                                  options=df.columns,
                                  placeholder=f"Choose target column for analysis",
                                  key="target_x",
                                  disabled=st.session_state["time_as_x"])
        col2.write("")
        col2.write("")
        time_as_x = col2.checkbox(label="Set Time as x-Axis", key="time_as_x")

        col1, col2 = st.columns(layout)

        color = col1.selectbox(label="Choose column for color differentiation",
                               options=df.columns,
                               placeholder=f"Choose color column for analysis",
                               key="color",
                               disabled=st.session_state["disable_color"])
        col2.write("")
        col2.write("")
        disable_color = col2.checkbox(label="Disable color parameter", key="disable_color")

        col1, col2 = st.columns(layout)

        hover_list = col1.multiselect(label="Choose columns for hover information",
                                      options=df.columns,
                                      placeholder="Choose columns for hover information",
                                      key="hover",
                                      disabled=st.session_state["disable_hover"])
        col2.write("")
        col2.write("")
        disable_hover = col2.checkbox(label="Disable hover parameter", key="disable_hover")

        with st.container(border=True):
            col1, col2 = st.columns(layout)
            col1.write("If this toggle is activated, missing data will be filled with 0. "
                     "This may or may not make sense in the context of research. Please make an informed decision.")
            toggle_fillna = col2.toggle(label="Fill data gaps with 0", key="toggle_fillna")

        plot_type = st.selectbox(label="Choose type of plot for visualisation",
                                 options=["Bar", "Box", "Scatter"])

        go_button = st.button(":blue[start plotting]", use_container_width=True)

    if toggle_fillna is True:
        plot_data = u.build_scatter_data(df)
    else:
        plot_data = df
    if time_as_x is True:
        target_x = c.DATE_START
    if disable_hover is True:
        hover_list = []
    if disable_color is True:
        color = c.HIST
        title = f"{target_y} over {target_x}"
        info = "Data before 2000, marked as historic, is to be considered of lesser quality!"
    else:
        title = f"{target_y} over {target_x} differentiated by {color}"
        info = f"{color} (color-parameter): {t.info_dict.get(color)}"
    if toggle_fillna is True:
        subtitle = "data gaps filled with 0 for visualisation"
    else:
        subtitle = "data gaps may exists and therefore an incomplete picture might be painted."

    if go_button:
        with st.container(border=True):
            st.write(":blue[View your custom plot]")
            if plot_type == "Scatter":
                plot = px.scatter(
                    plot_data,
                    x=target_x,
                    y=target_y,
                    color=color,
                    hover_data=hover_list,
                    title=title,
                    subtitle=subtitle)
                st.plotly_chart(plot)

            elif plot_type == "Box":
                plot = px.box(
                    plot_data,
                    x=target_x,
                    y=target_y,
                    color=color,
                    hover_data=hover_list,
                    title=title,
                    subtitle=subtitle)
                st.plotly_chart(plot)

            elif plot_type == "Bar":
                plot = px.bar(
                    plot_data,
                    x=target_x,
                    y=target_y,
                    color=color,
                    hover_data=hover_list,
                    title=title,
                    subtitle=subtitle)
                st.plotly_chart(plot)

            with st.container(border=True):
                st.write(":blue[Infobox on restrictions regarding the plot]")
                st.dataframe(info_table, hide_index=True, column_config={"0": "parameter", "1": "argument"})
                st.write(f'''
                {target_x} (x-axis): {t.info_dict.get(target_x)}  
                {target_y} (y-axis): {t.info_dict.get(target_y)}  
                {info}
                ''')

m.write_impressum()
