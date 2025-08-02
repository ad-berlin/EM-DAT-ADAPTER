import streamlit as st

from text.text_info import TEXT_ABOUT, emoji_dict

# setup of entire webpage, global settings
st.set_page_config(
    page_title="Visualising Disaster around the Globe",
    page_icon=emoji_dict.get('EMOJI_HEADER'),
    layout='wide',
    menu_items={
        'About': TEXT_ABOUT})

# single page setup
start_page = st.Page(  # data upload, general information about EM-DAT, useful tips
    page="pages/start.py",
    title="Start",
    icon='🦥',
    default=True)

dis_type_page = st.Page(  # visualisation per classification with different scopes (group, subgroup, type, or subtype)
    page="pages/dis_type.py",
    title="Per classification",
    icon='🐢',
    default=False)

region_page = st.Page(  # visualisation per region with different scopes (region, subregion, country, or location)
    page="pages/region.py",
    title="Per region",
    icon='🦒',
    default=False)

time_page = st.Page(
    page="pages/time.py",
    title="Over time",
    icon='🦛',
    default=False)

explore_page = st.Page(  # allow self conducted exploration based of free selection of column(s) and search terms
    page="pages/explore.py",
    title="Explore further",
    icon='🐺',
    default=False)

table_page = st.Page(  # view full table and restrict columns if needed
    page="pages/table.py",
    title="See full table",
    icon='🌪️',
    default=False)

data_page = st.Page(  # page for data quality e.g. show nans, compare nans per region etc.
    page="pages/data.py",
    title="Data quality",
    icon='🦖',
    default=False)

sources_page = st.Page(  # page listing all sources in full length
    page="pages/sources.py",
    title="Sources",
    icon='🦖',
    default=False)

process_page = st.Page(  # page explaining the process
    page="pages/process.py",
    title="The process",
    icon='🦖',
    default=False)

about_page = st.Page(  # page explaining the intention and vision
    page="pages/about.py",
    title="About",
    icon='🦖',
    default=False)

part_page = st.Page(  # page inviting to participate in the project, maybe linking to reddit
    page="pages/part.py",
    title="Participate",
    icon='🦖',
    default=False)

# st.logo("images/logo.png")  # TODO: fix logo sizing

# navigation and page-order
pg = st.navigation(
    pages={
        "Analysis": [
            start_page,  # TODO: maybe start page extra?; Can some pages be collapsed?
            dis_type_page,
            region_page,
            time_page,
            table_page,
            explore_page,
        ],
        "Meta Data": [
            data_page,  # add page for data quality e.g. show nans, compare nans per region etc.
            sources_page,  # add page listing all sources in full length
            process_page,  # add page explaining the process
        ],
        "About": [
            about_page,  # add page explaining the intention and vision
            part_page,  # add page inviting to participate in the project, maybe linking to reddit
        ]
    })

pg.run()  # run all pages


# add to sidebar: link referring where to download the EM-DAT data
st.sidebar.link_button(
    ":arrow_down: EM-DAT Data Download",
    url="https://public.emdat.be/",
    use_container_width=True)

# add to sidebar: link referring where find the homepage of the EM-DAT project
st.sidebar.link_button(
    ":globe_with_meridians: EM-DAT Project Website",
    url="https://www.emdat.be/",
    use_container_width=True)

# add to sidebar: link referring where to find the EM-DAT online documentation
st.sidebar.link_button(
    ":blue_book: EM-DAT Documentation",
    url="https://doc.emdat.be/",
    use_container_width=True)

st.sidebar.link_button(
    "➕ UN Data Download",
    url="https://population.un.org/wpp/downloads?folder=Standard%20Projections&group=CSV%20format",
    use_container_width=True)
