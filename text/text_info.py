from utils import constants as c

info_dict = {
    c.NUM: "Unique 8-digit identifier including the year (4 digits) and a sequential number (4 digits), with the ISO country code appended.",
    c.HIST: "Binary field specifying whether the disaster happened before 2000. Data before 2000 should be considered of lesser quality.",
    c.CLASS_KEY: "A unique 15-character string identifying disasters in terms of the Group Subgroup Type and Subtype classification hierarchy.",
    c.DIS_NAT_TECH: "The disaster group, i.e., ’Natural’ or ’Technological.’",
    c.DIS_SUBGROUP: "The disaster subgroup.",
    c.DIS_TYPE: "The disaster type.",
    c.DIS_SUBTYPE: "The disaster subtype.",
    c.EXT_ID: "List of identifiers pointing to external services and resources, such as the disaster Global Identifier (GLIDE) number.",
    c.NAME: "Short specification for disaster identification, e.g., storm names (e.g., ’Mitch’) plane type in air crash (e.g., ’Boeing 707’), disease name (e.g., ’Cholera’), or volcano name (e.g., ’Etna’).",
    c.ISO: "The International Organization for Standardization (ISO) 3-letter code referring to the Country. The ISO 3166 norm is used.",
    c.COUNTRY: "Country where the disaster occurred and had an impact using names from the UN M49 Standard.",
    c.SUBREGION: "Subregion where the disaster occurred based on UN M49 standard.",
    c.REGION: "Region where the disaster occurred based on UN M49 standard.",
    c.LOCATION: "Geographical location name as specified in the sources, e.g., city, village department, province, state, or district.",
    c.ORIGIN: "Additional specifications on the contextual factors that led to the event, e.g., ’heavy rains’ for floods or ’drought’ for a forest fire.",
    c.ASS_TYPES: "List of secondary disaster types cascading from or co-occurring aside from the main type, e.g., a landslide following a flood or an explosion after an earthquake.",
    c.OFDA_BHA: "Binary field specifying whether the Office of US Foreign Disaster Assistance (OFDA) responded to the disaster.",
    c.INTERNAT_ASSIST_REQ: "Binary field specifying whether there was a request for international assistance from the affected country.",
    c.EM_DECLARE: "Binary field specifying whether a state of emergency was declared in the country.",
    c.AID: "The total amount (in thousands of US dollars at the time of the report) of contributions for immediate relief activities to the country in response to the disaster, sourced from the Financial Tracking System of OCHA (1992–2015). Not maintained after 2015.",
    c.MAG: "Value related to the intensity of a hazard depending on the disaster type.",
    c.MAG_SCALE: "The associated unit for the Magnitude column.",
    c.LAT: "North-South coordinates mainly for earthquakes and volcanic activity. Sometimes reported for floods, landslides, and storms (mostly when associated with floods).",
    c.LONG: "East-West coordinates mainly for earthquakes and volcanic activity. Sometimes reported for floods, landslides, and storms (mostly when associated with floods).",
    c.RIVER: "Name of affected river basins typically used for floods.",
    c.YEAR_START: "Year of occurrence of the disaster.",
    c.MONTH_START: "Month of occurrence of the disaster.",
    c.DAY_START: "Day of occurrence of the disaster.",
    c.YEAR_END: "Year of disaster conclusion.",
    c.MONTH_END: "Month of conclusion of the disaster.",
    c.DAY_END: "Day of conclusion of the disaster.",
    c.DEATHS: "Total fatalities (deceased and missing combined).",
    c.INJURED: "Number of people with physical injuries, trauma, or illness requiring immediate medical assistance due to the disaster.",
    c.HOMELESS: "Number of people requiring shelter due to their houses being destroyed or heavily damaged during the disaster.",
    c.AFFECTED: "Not specified in documentation (https://doi.org/10.1016/j.ijdrr.2025.105509)",
    c.TOT_AFFECTED: "Total number of affected people (No. Injured, No. Affected, and No. Homeless combined).",
    c.RECONSTRUCTION: "Costs for replacement of lost assets in thousands of US dollars.",
    c.RECONSTRUCTION_ADJ: "Reconstruction costs in thousands of US dollars, adjusted for inflation using the Consumer Price Index (CPI).",
    c.INSURED: "Economic damage covered by insurance companies in thousands of US dollars.",
    c.INSURED_ADJ: "Insured damage in thousands of US dollars adjusted for inflation using the Consumer Price Index (CPI).",
    c.DAMAGE: "Value of all economic losses directly or indirectly due to the disaster in thousands of US dollars.",
    c.DAMAGE_ADJ: "Total damage in thousands of US dollars adjusted for inflation using the Consumer Price Index (CPI).",
    c.CPI: "Consumer Price Index from OECD used to adjust US dollars values for inflation relative to 'Start Year'.",
    c.ADMIN_UNITS: "Collection of impacted Administrative Units from the FAO GAUL 2015 referential. Individual objects correspond to Level-1 or Level-2 Administrative Units. Geocoding is maintained for non-biological natural hazards from 2000 onwards.",
    c.ENTRY_DATE: "The day on which the event record was created in EM-DAT.",
    c.UPDATE_DATE: "The last date of modification of the event or one of its associated records in EM-DAT.",
    c.NUMBER_EV: "Count of registered events per timespan and category e.g. 'Disaster Subtype'.",
    c.DIS_DURATION: "Difference between 'Start Date' and 'End Date' in days plus one.",
    c.DATE_START: "Start date of occurrence of the disaster (if day is missing set to first of month; if month is missing set to first of year)",
    c.DATE_END: "End date of conclusion of the disaster (if day is missing set to first of month; if month is missing set to first of year)",
    c.CONTINENT_R: "Continent where the disaster occurred.",
    c.M49_CODE_R: "Code of the region where the disaster occurred (UN M49 standard).",
    c.UN_M49_IR: "Intermediate region where the disaster occurred based on UN M49 standard.",
    c.M49_CODE_IR: "Code of the intermediate region where the disaster occurred (UN M49 standard).",
    c.GEOGRAPH_SR: "Geographical subregion where the disaster occurred.",
    c.M49_CODE_SR: "Code of the subregion where the disaster occurred (UN M49 standard).",
    c.M49_CODE_C: "Code of the country where the disaster occurred (UN M49 standard).",
    c.ADMIN_C: "Administrative location/region where the disaster occurred.",
    c.SOVEREIGN_C: "Sovereign country where the disaster occurred according to UN 2025.",
    c.UN_M49_C: "Code of the sovereign country where the disaster occurred (UN M49 standard).",
    c.ISO_A2: "The International Organization for Standardization (ISO) 2-letter code referring to the country. The ISO 3166 norm is used.",
    c.ISO_A3: "The International Organization for Standardization (ISO) 3-letter code referring to the country. The ISO 3166 norm is used.",
    c.ORIGIN_CLEAN: "'Origin'-Column treated for spelling and meaning.",
    c.ORIGIN_LABEL: "'Origin'-Column reduced to specific labels.",
}

explain_dict = {
    c.DIS_DURATION: "To be able to compare disasters in intensity and impact a duration variable can be helpful.",
    c.DATE_START: "A start date is necessary to sort events by occurrence in time.",
    c.DATE_END: "An end date can be interesting to sort events by occurrence in time.",
    c.CONTINENT_R: "Additionally to the 'M49 Regions' can a comparison by Continent come handy for analysis.",
    c.M49_CODE_R: "The statistical codes used in the M49 standard are globally used and allow easy recognition of regions.",
    c.UN_M49_IR: "Additionally to the 'M49 Subregions' can a comparison by M49 intermediate regions come handy for analysis.",
    c.M49_CODE_IR: "The statistical codes used in the M49 standard are globally used and allow easy recognition of regions.",
    c.GEOGRAPH_SR: "Additionally to the 'M49 Subregions' can a comparison by geographical subregion come handy for analysis.",
    c.M49_CODE_SR: "The statistical codes used in the M49 standard are globally used and allow easy recognition of regions.",
    c.M49_CODE_C: "The statistical codes used in the M49 standard are globally used and allow easy recognition of regions.",
    c.ADMIN_C: "Additionally to the 'M49 Countries' can a comparison by administrative regions come handy for analysis.",
    c.SOVEREIGN_C: "Additionally to the 'M49 Countries' can a comparison by UN sovereign countries come handy for analysis.",
    c.UN_M49_C: "This column shows only countries that are in the most recent version of the M49 standard.",
    c.ISO_A2: "The codes given by the International Organization for Standardization (ISO) are globally used and allow easy recognition of regions.",
    c.ISO_A3: "The codes given by the International Organization for Standardization (ISO) are globally used and allow easy recognition of regions.",
    c.ORIGIN_CLEAN: "As explained in 'The Process' the column Origin is treated to allow better analysis. This is a clean version, but still containing very detailed information.",
    c.ORIGIN_LABEL: "As explained in 'The Process' the column Origin is treated to allow better analysis. This column contains labels.",
}

TEXT_INTRO = '''
DisTrack aims to visualise disaster data in a meaningful way and is only usable with the data of the EM-
DAT database. Other uploads will generate errors.

The database EM-DAT is compiled from various sources, including UN agencies,
non-governmental organizations, reinsurance companies, research institutes,
and press agencies [1]. The Centre for Research on the Epidemiology of Disasters
(CRED) distributes the data in open access for non-commercial use.

EM-DAT globally records at the country level human and economic
losses for disasters with at least one of the following criteria: 
- 10 fatalities;
- 100 affected people;
- a declaration of state of emergency;
- a call for international assistance. [1]

This app only allows analysis and display of disasters with a natural disaster agent.
'''

TEXT_ABOUT = '''
This app has been developed to allow an insightful analysis of disaster data. This app has
been developed in 2025/2026 and is inspired by the first app for EM-DAT visualisation by
Damien Delforge. [1]

Thanks go to all the experts who participated in the design process and contributed valuable input/feedback through
survey and/or interview. All contributors are if not wished otherwise listed below.
'''

TEXT_IMPRESSUM = '''
:blue[Declaration of competing interest]  
The author declares no known competing financial interests or personal relationships that could have appeared to 
influence the work reported in this project.  
Diaz, 2025
'''

TEXT_HELP = '''
HELP - How to find my way around?
'''

help_dict = {
    'HELP_START': '''
    This page allows you to upload the EM-DAT data.
    
    1. Please access the data via the official website of the CRED.
    2. You will need to register with the CRED to be able to access the data.
    3. Download the full dataset to avoid any complications.
    4. Upload the excel file as it is at the end of this page and wait for the green massage of success stating:
    File upload successful! This application will only work with this particular data set.
    5. You then can move on to the analysing parts of this application.
    
    Enjoy!
    ''',

    'HELP_DIS_TYPE': '''
    This page allows you to analyse disaster occurrence and impact through the classification of disasters.
    
    This page is split into four parts. The first is global settings, the second is an overview, the third is a deeper
    analysis, and the last is a comparison.
    
    1. Global settings allow to choose scope, and timespan.
    2. The overview allows you to choose a parameter which will be used as y-axis in the following plot. A definition of
    the chosen parameter will be provided directly below. Data gaps, as omnipresent as they are, are filled with 0 to
    make the event itself visible in the plot. Before referring to those events stating 0 as a value, please check with
    the Disaster Number of the event.
    3. The deeper analysis allows you to choose specific classifications you deem interesting. Each of them will open in
    a separate tab. In each tab you can choose multiple parameters to explore. They will all open in the order chosen
    below. Switching between tabs is possible and the selection will remain. Changes in the global settings will lead to
    a reset in the selected classifications and parameters.
    4. The comparison allows you to choose multiple classifications to compare. Those will be visible in three tabs
    each visualizing the same information. One time in box plots, one in a histogram, and one in a table. Please be
    cautious using the comparison mechanism for magnitudes. If unsure about the unit of magnitude please look up the
    classifications in question in part 3.
    
    All plots will can be downloaded using the camera icon appearing in the upper right corner if the cursor is moved
    over the plot. All separate colors in the legend on the right side in the plots can be separated by double click.
    This can be reversed by double clicking again. Disabling or enabling separate colors in the legend on the right side
    can be done with single clicks. Tables can be saved as CSV by using the download button in the upper right corner
    of the table.
    ''',

    'HELP_REGION': '''
    This page allows you to analyse disaster occurrence and impact through the region of occurrence of disasters.
    
    This page is split into four parts. The first is global settings, the second is an overview, the third is a deeper
    analysis, and the last is a comparison.
    
    1. Global settings allow to choose scope, grouping, and timespan.
    2. The overview allows you to choose a parameter which will be used as y-axis in the following plot. A definition of
    the chosen parameter will be provided directly below. Data gaps, as omnipresent as they are, are filled with 0 to
    make the event itself visible in the plot. Before referring to those events stating 0 as a value, please check with
    the Disaster Number of the event.
    3. The deeper analysis allows you to choose specific regions you deem interesting. Each of them will open in
    a separate tab. In each tab you can choose multiple parameters to explore. They will all open in the order chosen
    below. Switching between tabs is possible and the selection will remain. Changes in the global settings will lead to
    a reset in the selected regions and parameters.
    4. The comparison allows you to choose multiple regions to compare per Disaster Type. Those regions will be visible
    in three tabs each visualizing the same information. One time in box plots, one in a histogram, and one in a table.
    Please be cautious using the comparison mechanism for magnitudes. If unsure about the unit of magnitude please
    look up the classifications in question in part 3.
    
    All plots will can be downloaded using the camera icon appearing in the upper right corner if the cursor is moved
    over the plot. All separate colors in the legend on the right side in the plots can be separated by double click.
    This can be reversed by double clicking again. Disabling or enabling separate colors in the legend on the right side
    can be done with single clicks. Tables can be saved as CSV by using the download button in the upper right corner
    of the table.
    ''',

    'HELP_TABLE': '''
    This page allows you to access the full data set as it would be in an excel file.
    
    This page is split into two parts. The first gives you specific disasters, if you provide the exact Disaster Number.
    The second allows you to filter the data and download the table as an excel file.
    ''',

    'HELP_EXPLORE': '''
    This page allows you to filter the data as you need it and build your own plots. It is definitely more possible,
    than what is useful.
    
    All plots will can be downloaded using the camera icon appearing in the upper right corner if the cursor is moved
    over the plot. All separate colors in the legend on the right side in the plots can be separated by double click.
    This can be reversed by double clicking again. Disabling or enabling separate colors in the legend on the right side
    can be done with single clicks.
    '''
}

HEADER = ":red[Beta:] :blue[DisTrack - International Disaster Analysis]"

SELECT_REGION = '''Choose Region'''

SELECT_SUBREGION = '''Choose Subregion'''

SELECT_COUNTRY = '''Choose Country'''

SELECT_LOCAL = '''Choose Focus Regions'''

SELECT_DIS_SCOPE = '''Choose Scope'''

SELECT_TIME = '''Choose Timespan of Interest'''

SELECT_GROUPING = '''Choose Grouping'''

SELECT_PARAM_OV = '''Choose Parameter for Overview'''

SELECT_PARAM_COM = '''Choose Parameter for Comparison'''

ERROR_DATA = '''🚨 Please, upload your dataset first on the start page!'''

ERROR_VALUE = '''Not enough data for insightful display...'''

month_dict = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

### area for spelling preprocessing

spell_aim_list = ["rain", "heavy", "rainfall", "rains", "snowmelt", "monsoon", "monsoonal", "lightning",
                  "torrential", "temperature", "thunderstorm", "continuous", "wind", "precipitation", "storm",
                  "drought", "typhoon", "tropical", "season", "seasonal", "mei-yu", "insufficient", "volcano"]

word_origin_map = {
    # synonyms label
    "rainfall": "rain",
    "rains": "rain",
    "showers": "rain",
    "precipitation": "rain",
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
    "extended": "continuous",
    # category synonyms "irregular"
    "erratic": "irregular",
    # category synonyms "insufficient"
    "poor": "insufficient",
    "limited": "insufficient",
    "below-average": "insufficient",
    "reduced": "insufficient",
    "scarcity_of": "insufficient",
    "lack_of": "insufficient",
    "lack": "insufficient",
}

mapping_origin_labels = {
    "la ": "la nina",
    "el ": "el nino",
    "tropical": "tropical depression",
    "sanitation": "sanitation/hygiene/safe water",
    "melt": "melting snow",
    "dam": "dam/levy break/release",
    "front": "cold front",
    "snow": "snow fall",
    "rainstorm": "rain event",
    "seasonal": "rain event",
    "continuous": "rain event",
    "torrential": "rain event",
    "extreme": "rain event",
    "irregular": "drought/insufficient rain",
    "insufficient": "drought/insufficient rain",
    "low": "drought/insufficient rain",
    "fail": "drought/insufficient rain",
    "poor": "drought/insufficient rain",
    "drought": "drought/insufficient rain",
    "heat": "heat/high temperatures",
    "high": "heat/high temperatures",
    "low temper": "cold/low temperatures",
    "pressure": "low pressure area (LPA)",
    "wind": "storm/strong wind",
    "storm": "storm/strong wind",
    "surge": "storm surge",
    "ice": "ice jam",
    "earthquake": "earthquake/seismic activity",
    "weather": "weather (unspecified)",
    "unclear": "unclear origin (check with original sources)"
}

one_word_descriptor_lst = [
    "typhoon",  # label as in list
    "cyclone",  # label as in list
    "monsoon",  # label as in list
    "hurricane",  # label as in list
    "mei-yu",  # label as in list
    "landslide",  # label as in list
    "volcano",  # label as in list
    "hail",  # label as in list
    "lightning",  # label as in list
    "thunderstorm",  # label as in list
    "flood",  # label as in list
    "tornado",  # label as in list
    "no data",  # label as in list
]

two_word_descriptor_lst = [
    ("la ", "nina"),  # la nina
    ("el ", "nino"),  # el nino
    ("melt", "snow"),  # melting snow
    ("tropical", "depression"),  # tropical depression
    ("dam", "break"),  # dam/levy break/release
    ("dam", "release"),  # dam/levy break/release
    ("dam", "opening"),  # dam/levy break/release
    ("front", "cold"),  # cold front
    ("pressure", "low"),  # low pressure area (LPA)
    ("wind", "extreme"),  # storm/strong wind
    ("surge", "storm"),  # storm surge
    ("ice", "jam")  # ice jam
]

rain_descriptor_lst = [
    "extreme",  # rain event
    "torrential",  # rain event
    "continuous",  # rain event
    "seasonal",  # rain event
    "fail",  # drought/insufficient rain
    "insufficient",  # drought/insufficient rain
    "poor",  # drought/insufficient rain
    "irregular",  # drought/insufficient rain
]

complex_label_lst = [
    ["sanitation", "sanitary", "hygien", "dirty water", "drinking water", "safe water", "contaminat", "clean water"],
    # sanitation/hygiene/safe water
    ["rainstorm", "monsoon", "mei-yu"],  # rain event
    ["drought", "dry", "low rain"],  # drought/insufficient rain
    ["heat", "hot", "high temper"],  # heat/high temperatures
    ["storm", "wind", "typhoon", "hurricane", "thunderstorm"],  # storm/strong wind
    ["earthquake", "seismic", "tremor"],  # earthquake/seismic activity
    ["weather", "meteorological"],  # weather (unspecified)
    ["low temper"]  # cold/low temperatures
]

### countries, political processing

# historic labels comparable in borders
country_label_dict = {
    "Czech Republic": "Czechia",
    # "China, Hong Kong Special Administrative Region": "Hong Kong",
    # "China, Macao Special Administrative Region": "Macao",
    "German Democratic Republic": "Germany",
    "Germany Federal Republic": "Germany",
    "Kosovo": "Kosovo*",
    "People's Democratic Republic of Yemen": "Yemen",
    "Taiwan (Province of China)": "Taiwan",
    "Yemen Arab Republic": "Yemen",
    # "State of Palestine": "Palestine",
    "Czechoslovakia": "Czechoslovakia (historic)",
    "Netherlands Antilles": "Netherlands Antilles (historic)",  # caribbean
    "Serbia Montenegro": "Serbia Montenegro (historic)",  # southern europe
    "Soviet Union": "Soviet Union (historic)",  # east europe
    "Yugoslavia": "Yugoslavia (historic)",  # southern europe
}
