import streamlit as st

# setup of entire webpage, global settings
st.set_page_config(
    page_title="DisTrack - Visualising Disaster",
    page_icon="🦖",
    layout='wide')

# single page setup
start_page = st.Page(  # data upload, general information about EM-DAT, useful tips
    page="pages/start.py",
    title="Start",
    icon=":material/home:",
    default=True)

dis_type_page = st.Page(  # visualisation per classification with different scopes (group, subgroup, type, or subtype)
    page="pages/dis_type.py",
    title="Per Classification",
    icon=":material/category:",  # /modeling, /schema, /category
    default=False)

region_page = st.Page(  # visualisation per region with different scopes (region, subregion, country, or location)
    page="pages/region.py",
    title="Per Region",
    icon=":material/public:",  # /captive_portal, /public
    default=False)

explore_page = st.Page(  # allow self conducted exploration based of free selection of column(s) and search terms
    page="pages/explore.py",
    title="Explore Further",
    icon=":material/star:",  # /star, /search, /travel_explore
    default=False)

table_page = st.Page(  # view full table and restrict columns if needed
    page="pages/table.py",
    title="View Table",
    icon=":material/table:",
    default=False)

data_page = st.Page(  # page for data quality e.g. show nans, compare nans per region etc.
    page="pages/data.py",
    title="Data Quality",
    icon=":material/fact_check:",
    default=False)

sources_page = st.Page(  # page listing all sources in full length
    page="pages/sources.py",
    title="Sources",
    icon=":material/link:",  # /link, /library_books
    default=False)

process_page = st.Page(  # page explaining the process
    page="pages/process.py",
    title="The Process",
    icon=":material/route:",  # /route, /manufacturing
    default=False)

about_page = st.Page(  # page explaining the intention and vision
    page="pages/about.py",
    title="About",
    icon=":material/verified:",  # /science, /verified
    default=False)

policy_page = st.Page(  # page explaining the situation with the countries and regions
    page="pages/policy.py",
    title="Definitions and Terminology",
    icon=":material/menu_book:",
    default=False)

part_page = st.Page(  # page inviting to participate in the project, maybe linking to reddit
    page="pages/part.py",
    title="Participate",
    icon=":material/groups:",  # /groups, /handshake
    default=False)

# navigation and page-order
pg = st.navigation(
    pages={
        "Analysis": [
            start_page,
            dis_type_page,
            region_page,
            table_page,
            explore_page,
        ],
        "Meta Data": [
            data_page,  # add page for data quality e.g. show nans, compare nans per region etc.
            process_page,  # add page explaining the process
            policy_page, # add page explaining the situation with the countries and regions
            sources_page,  # add page listing all sources in full length
        ],
        "About DisTrack": [
            about_page,  # add page explaining the intention and vision
            part_page,  # add page inviting to participate in the project, maybe linking to reddit
        ]
    })

pg.run()  # run all pages


# add to sidebar: link referring where find the homepage of the EM-DAT project
st.sidebar.link_button(
    "EM-DAT Project Website",
    url="https://www.emdat.be/",
    use_container_width=True)

# add to sidebar: link referring where to find the EM-DAT online documentation
st.sidebar.link_button(
    "EM-DAT Documentation",
    url="https://doc.emdat.be/",
    use_container_width=True)

# st.sidebar.image(image="images/logo_ver_1.png", width=250)  # TODO: fix logo sizing
