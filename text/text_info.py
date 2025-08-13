info_dict = {
    "DisNo.": "Unique 8-digit identifier including the year (4 digits) and a sequential number (4 digits), with the ISO country code appended.",
    "Historic": "Binary field specifying whether the disaster happened before 2000. Data before 2000 should be considered of lesser quality.",
    "Classification Key": "A unique 15-character string identifying disasters in terms of the Group Subgroup Type and Subtype classification hierarchy.",
    "Disaster Group": "The disaster group, i.e., ’Natural’ or ’Technological.’",
    "Disaster Subgroup": "The disaster subgroup.",
    "Disaster Type": "The disaster type.",
    "Disaster Subtype": "The disaster subtype.",
    "External IDs": "List of identifiers pointing to external services and resources, such as the disaster Global Identifier (GLIDE) number.",
    "Event Name": "Short specification for disaster identification, e.g., storm names (e.g., ’Mitch’) plane type in air crash (e.g., ’Boeing 707’), disease name (e.g., ’Cholera’), or volcano name (e.g., ’Etna’).",
    "ISO": "The International Organization for Standardization (ISO) 3-letter code referring to the Country. The ISO 3166 norm is used.",
    "Country": "Country where the disaster occurred and had an impact using names from the UN M49 Standard.",
    "Subregion": "Subregion where the disaster occurred based on UN M49 standard.",
    "Region": "Region where the disaster occurred based on UN M49 standard.",
    "Location": "Geographical location name as specified in the sources, e.g., city, village department, province, state, or district.",
    "Origin": "Additional specifications on the contextual factors that led to the event, e.g., ’heavy rains’ for floods or ’drought’ for a forest fire.",
    "Associated Types": "List of secondary disaster types cascading from or co-occurring aside from the main type, e.g., a landslide following a flood or an explosion after an earthquake.",
    "OFDA/BHA Response": "Binary field specifying whether the Office of US Foreign Disaster Assistance (OFDA) responded to the disaster.",
    "Appeal": "Binary field specifying whether there was a request for international assistance from the affected country.",
    "Declaration": "Binary field specifying whether a state of emergency was declared in the country.",
    "AID Contribution ('000 US$)": "The total amount (in thousands of US$ at the time of the report) of contributions for immediate relief activities to the country in response to the disaster, sourced from the Financial Tracking System of OCHA (1992–2015). Not maintained after 2015.",
    "Magnitude": "Value related to the intensity of a hazard depending on the disaster type.",
    "Magnitude Scale": "The associated unit for the Magnitude column.",
    "Latitude": "North-South coordinates mainly for earthquakes and volcanic activity. Sometimes reported for floods, landslides, and storms (mostly when associated with floods).",
    "Longitude": "East-West coordinates mainly for earthquakes and volcanic activity. Sometimes reported for floods, landslides, and storms (mostly when associated with floods).",
    "River Basin": "Name of affected river basins typically used for floods.",
    "Start Year": "Year of occurrence of the disaster.",
    "Start Month": "Month of occurrence of the disaster.",
    "Start Day": "Day of occurrence of the disaster.",
    "End Year": "Year of disaster conclusion.",
    "End Month": "Month of conclusion of the disaster.",
    "End Day": "Day of conclusion of the disaster.",
    "Total Deaths": "Total fatalities (deceased and missing combined).",
    "No. Injured": "Number of people with physical injuries, trauma, or illness requiring immediate medical assistance due to the disaster.",
    "No. Homeless": "Number of people requiring shelter due to their houses being destroyed or heavily damaged during the disaster.",
    "No. Affected": "Not specified in documentation (https://doi.org/10.1016/j.ijdrr.2025.105509)",
    "Total Affected": "Total number of affected people (No. Injured, No. Affected, and No. Homeless combined).",
    "Reconstruction Costs ('000 US$)": "Costs for replacement of lost assets in thousands of US dollars (’000 US$).",
    "Reconstruction Costs, Adjusted ('000 US$)": "Reconstruction Costs (‘000 US$), adjusted for inflation using the Consumer Price Index (CPI).",
    "Insured Damage ('000 US$)": "Economic damage covered by insurance companies in thousands of US dollars (’000 US$).",
    "Insured Damage, Adjusted ('000 US$)": "Insured Damage (’000 US$) adjusted for inflation using the Consumer Price Index (CPI).",
    "Total Damage ('000 US$)": "Value of all economic losses directly or indirectly due to the disaster in thousands of US dollars (’000 US$).",
    "Total Damage, Adjusted ('000 US$)": "Total Damage (’000 US$) adjusted for inflation using the Consumer Price Index (CPI).",
    "CPI": "Consumer Price Index from OECD used to adjust US$ values for inflation relative to Start Year.",
    "Admin Units": "Collection of impacted Administrative Units from the FAO GAUL 2015 referential. Individual objects correspond to Level-1 or Level-2 Administrative Units. Geocoding is maintained for non-biological natural hazards from 2000 onwards.",
    "Entry Date": "The day on which the event record was created in EM-DAT.",
    "Last Update": "The last date of modification of the event or one of its associated records in EM-DAT.",
    "Duration of Disaster": "Difference between start date and end date in days.",
    "Number of Events": "Count of registered events per timespan and category e.g. Disaster Subtype."
}

TEXT_INTRO = '''
The database EM-DAT is compiled from various sources, including UN agencies,
non-governmental organizations, reinsurance companies, research institutes,
and press agencies. The Centre for Research on the Epidemiology of Disasters
(CRED) distributes the data in open access for non-commercial use.

EM-DAT globally records at the country level human and economic
losses for disasters with at least one of the following criteria: 
- 10 fatalities;
- 100 affected people;
- a declaration of state of emergency;
- a call for international assistance.

This app only allows analysis and display of disasters with a natural disaster agent.
'''

TEXT_ABOUT = '''
This app has been developed to allow an insightful analysis of disaster data. This app has
been developed by Anais Diaz in 2025/2026 and is inspired by the first app for EM-DAT visualisation by
Damien Delforge.

Thanks go to all the experts who participated in the design process and contributed valuable input/feedback through
survey and/or interview. All contributors are if not wished otherwise listed below.
'''

TEXT_LIFE = '''
Explore data with caution! Behind every number hides a life!
'''

TEXT_IMPRESSUM = '''
:blue[Impressum]

Declaration of competing interest  
The author declares no known competing financial interests or personal relationships that could have appeared to 
influence the work reported in this project.

:violet[Anais Diaz, 2025]
'''

TEXT_HELP = '''
HELP: How to find my way around!
'''

help_dict = {
    'HELP_DIS_TYPE': '''
    to be filled
    ''',

    'HELP_REGION': '''
    *Country*  
    The term "Country" is not as neutral as one could wish, which is why multiple definitions are available
    here.    
    :blue[UN Sovereign Countries] - The dataset is reduced to the 193 states of the UN council from 2025. The territories
    are as described by the UN (source: ...)  
    :blue[EM-DAT Countries] - The dataset is not manipulated and the labels as given by the CRED are used. (source: ...)  
    :blue[Administrative Regions] - Regions which have special administrative status, are under occupation, or are overseas
    territory are separated from their main land to allow individual analysis. (source: ...)  
    :blue[UN M49 Countries] - Countries  are defined as in the UN M49 standard. (source: ...)
    
    *Subregion*  
    Based on "Countries" "Subregions" can be diverged. These are subjective groupings for broader pattern analysis. To
    begin with, two groupings are provided.  
    :blue[Geographical Subregions] - The aim is to group countries by shared geographical traits, locations, and/or water
    sources. (source: ...)  
    :blue[UN M49 Subregions] - Subregions are defined as in the UN M49 standard. (source: ...)
    
    *Region*  
    Based on "Subregions" "Regions" can be diverged. These are subjective groupings for broader pattern analysis. To
    begin with, two groupings are provided.  
    :blue[Continents] - The aim is to group countries by shared geographical traits, locations, and/or water
    sources.  
    :blue[UN M49 Regions] - Regions are defined as in the UN M49 standard. (source: ...)
    
    All of these definitions should support representation of human beings and their suffering through disasters.
    If important definitions are missing or active definitions are lacking or offending, please do not hesitate to
    inform the developer and provide data and/or sources to further improve this web tool.
    ''',

    'HELP_TABLE': '''
    to be filled
    ''',

    'HELP_EXPLORE': '''
    to be filled
    '''
}

SELECT_REGION = '''🌍 Choose Region'''

SELECT_SUBREGION = '''🌍 Choose Subregion'''

SELECT_COUNTRY = '''🌍 Choose Country'''

SELECT_LOCAL = '''📍 Choose Focus Regions'''

SELECT_DIS_SCOPE = '''🔍 Choose Scope'''

SELECT_TIME = '''⏱️ Timespan of Interest'''

SELECT_GROUPING = '''🧩 Choose Grouping'''

SELECT_PARAM = '''🐢 Choose Parameter'''

ERROR_DATA = '''🚨 Please, upload your dataset first on the start page!'''


emoji_dict = {
'EMOJI_HEADER' : '🦖',
'EMOJI_SUBHEADER' : '🦖'  # 🪳, 🦥
}

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