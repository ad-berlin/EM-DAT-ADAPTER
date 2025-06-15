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
    icon=emoji_dict.get('EMOJI_SUBHEADER'),
    default=True)

dis_type_page = st.Page(  # visualisation per classification with different scopes (group, subgroup, type, or subtype)
    page="pages/dis_type.py",
    title="Per classification",
    icon=emoji_dict.get('EMOJI_SUBHEADER'),
    default=False)

region_page = st.Page(  # visualisation per region with different scopes (region, subregion, country, or location)
    page="pages/region.py",
    title="Per region",
    icon=emoji_dict.get('EMOJI_SUBHEADER'),
    default=False)

time_page = st.Page(
    page="pages/time.py",
    title="Over time",
    icon=emoji_dict.get('EMOJI_SUBHEADER'),
    default=False)

explore_page = st.Page(  # allow self conducted exploration based of free selection of column(s) and search terms
    page="pages/explore.py",
    title="Explore further",
    icon=emoji_dict.get('EMOJI_SUBHEADER'),
    default=False)

table_page = st.Page(  # view full table and restrict columns if needed
    page="pages/table.py",
    title="See full table",
    icon=emoji_dict.get('EMOJI_SUBHEADER'),
    default=False)


# navigation and page-order
pg = st.navigation(
    pages=[
        start_page,
        dis_type_page,
        region_page,
        time_page,
        explore_page,
        table_page
        ])

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
