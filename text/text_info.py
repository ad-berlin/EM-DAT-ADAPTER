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
    "Last Update": "The last date of modification of the event or one of its associated records in EM-DAT",
    "Duration of Disaster": "Difference between start date and end date in days."
}

TEXT_INTRO = '''
The database is compiled from :blue-background[various sources], including UN agencies,
non-governmental organizations, reinsurance companies, research institutes,
and press agencies. The :blue-background[Centre for Research on the Epidemiology of Disasters
(CRED)] distributes the data in open access for :blue-background[non-commercial use].

EM-DAT globally records at the country level human and economic
losses for disasters with :blue-background[at least one of the following criteria]: 
- 10 :red[fatalities];
- 100 :orange[affected people];
- a declaration of :blue[state of emergency];
- a call for :green[international assistance].

For more information: *https://doi.org/10.1016/j.ijdrr.2025.105509*  
Source: EM-DAT, CRED / UCLouvain, Brussels, Belgium – www.emdat.be
'''

TEXT_ABOUT = '''
This app has been developed to allow an insightful analysis of disaster data. This app has
been developed by Anais Diaz in 2025 and is inspired by the first app for EM-DAT visualisation by
Damien Delforge.
'''

TEXT_LIVE = '''
Explore data with caution! Behind every number hides a life!
'''

TEXT_IMPRESSUM = '''
:blue[**Impresum**]

**Declaration of competing interest**  
*The author declares no known competing financial interests or personal relationships that could have appeared to 
influence the work reported in this project.*

:violet[**Anais Diaz, 2025**]
'''

TEXT_HELP = '''
HELP: How to find my way around!
'''

help_dict = {
    'HELP_DIS_TYPE' : '''to be filled''',
    'HELP_REGION': '''to be filled''',
    'HELP_TIME': '''to be filled''',
    'HELP_TABLE': '''to be filled''',
    'HELP_EXPLORE': '''to be filled''',
}

select_dict = {
'SELECT_REGION' : '''
🌍 Choose Region
''',

'SELECT_SUBREGION' : '''
🌍 Choose Subregion
''',

'SELECT_COUNTRY' : '''
🌍 Choose Country
''',

'SELECT_LOCAL' : '''
📍 Choose Focus Regions
''',

'SELECT_DIS_SCOPE' : '''
🔍 Choose Scope
''',

'SELECT_TIME' : '''
⏱️ Timespan of Interest
''',

'SELECT_GROUPING' : '''
🧩 Choose Grouping
'''
}


emoji_dict = {
'EMOJI_HEADER' : '🦥',

'EMOJI_SUBHEADER' : '🦖'  # 🪳
}


error_dict = {
'ERROR_DATA' : '''
🚨 Please, upload your dataset first on the start page!
''',

'ERROR_FILTER' : '''
🚨 Your chosen filters are too specific to plot. Please,
generalise your request!
'''
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

# UN comprehensive sovereign states "english name" to "english name (self-given name)"
country_local_name_un_2025_dict = {
    # A
    "Afghanistan": "Afghanistan (Afġānistān/ أَفْغَانِسْتَان)",
    "Albania": "Albania (Shqipëri)",
    "Algeria": "Algeria (Al Jazā’ir/ الجزائر)",
    "Andorra": "Andorra",
    "Angola": "Angola",
    "Antigua and Barbuda": "Antigua and Barbuda",
    "Argentina": "Argentina",
    "Armenia": "Armenia (Հայաստան/ Hayastan)",
    "Australia": "Australia",
    "Austria": "Austria (Österreich)",
    "Azerbaijan": "Azerbaijan (Azərbaycan)",
    # B
    "Bahamas": "Bahamas",
    "Bahrain": "Bahrain (Al Baḥrayn/ البحرين)",
    "Bangladesh": "Bangladesh (বাংলাদেশ)",
    "Barbados": "Barbados",
    "Belarus": "Belarus (Беларусь/ Bielaruś)",
    "Belgium": "Belgium (België)",
    "Belize": "Belize",
    "Benin": "Benin (Bénin)",
    "Bhutan": "Bhutan (འབྲུག/ Druk yul)",  # double check!
    "Bolivia": "Bolivia",
    "Bosnia and Herzegovina": "Bosnia and Herzegovina (Bosna i Hercegovina)",
    "Botswana": "Botswana",
    "Brazil": "Brazil (Brasil)",
    "Brunei Darussalam": "Brunei Darussalam",
    "Bulgaria": "Bulgaria (България)",
    "Burkina Faso": "Burkina Faso",
    "Burundi": "Burundi",
    # C
    "Cabo Verde": "Cabo Verde",
    "Cambodia": "Cambodia (កម្ពុជា/ Kâmpŭchéa)",  # double check!
    "Cameroon": "Cameroon (Cameroun)",
    "Canada": "Canada",
    "Central African Republic": "Central African Republic (République centrafricaine)",
    "Chad": "Chad (Tchad/ تشاد)",
    "Chile": "Chile",
    "China": "China (中國/ Zhōngguó)",
    "Colombia": "Colombia",
    "Comoros": "Comoros (جزر القمر/ Al Qamar)",
    "Congo": "Congo",
    "Costa Rica": "Costa Rica",
    "Côte d'Ivoire": "Côte d'Ivoire",
    "Croatia": "Croatia (Hrvatska)",
    "Cuba": "Cuba",
    "Cyprus": "Cyprus (Κύπρος/ Kýpros)",
    "Czechia": "Czechia (Česko)",
    # D
    "Democratic Republic of the Congo": "D.R. of the Congo (R.d. du Congo)",
    "Denmark": "Denmark (Danmark)",
    "Djibouti": "Djibouti (جيبوتي/ Jibuti)",
    "Dominica": "Dominica",
    "Dominican Republic": "Dominican Republic (Dominicana)",
    # E
    "Ecuador": "Ecuador",
    "Egypt": "Egypt (مصر/ Miṣr)",
    "El Salvador": "El Salvador",
    "Equatorial Guinea": "Equatorial Guinea (Guinée Équatoriale)",
    "Eritrea": "Eritrea (إريتريا/ Iritriya)",
    "Estonia": "Estonia (Eesti)",
    "Eswatini": "Eswatini",
    "Ethiopia": "Ethiopia (Ityop'iya)",
    # F
    "Fiji": "Fiji (Na Viti)",  # double check!
    "Finland": "Finland (Suomi)",
    "France": "France",
    # G
    "Gabon": "Gabon",
    "Gambia": "Gambia",
    "Georgia": "Georgia (საქართველო/ Sakartvelo)",
    "Germany": "Germany (Deutschland)",
    "Ghana": "Ghana",
    "Greece": "Greece (Ελλάδα)",
    "Grenada": "Grenada",
    "Guatemala": "Guatemala",
    "Guinea": "Guinea (Guinée)",
    "Guinea-Bissau": "Guinea-Bissau (Guiné-Bissau)",
    "Guyana": "Guyana",
    # H
    "Haiti": "Haiti (Haïti)",
    "Honduras": "Honduras",
    "Hungary": "Hungary (Magyarország)",
    # I
    "Iceland": "Iceland (Ísland)",
    "India": "India (भारत/ Bhārat)",  #  double check!
    "Indonesia": "Indonesia ",
    "Iran": "Iran (ایران/ Īrān)",
    "Iraq": "Iraq (العراق/ Al'Irāq)",
    "Ireland": "Ireland (Éire)",  # double check!
    "Israel": "Israel (יִשְׂרָאֵל / إسرائيل/ Isrā'īl)",  # double check!
    "Italy": "Italy (Italia)",
    # J
    "Jamaica": "Jamaica",
    "Japan": "Japan (日本/ Nippon/ Nihon)",
    "Jordan": "Jordan (الأردن/ Al-Urdunn)",
    # K
    "Kazakhstan": "Kazakhstan (Қазақстан)",
    "Kenya": "Kenya",
    "Kiribati": "Kiribati",
    "Kuwait": "Kuwait (الكويت/ Al-Kuwayt)",
    "Kyrgyzstan": "Kyrgyzstan (Кыргызстан)",
    # L
    "Lao People's D.R.": "Lao People's D.R. (ລາວ)",  # double check!
    "Latvia": "Latvia (Latvija)",
    "Lebanon": "Lebanon (لبنان/ Lubnān)",
    "Lesotho": "Lesotho",
    "Liberia": "Liberia",
    "Libya": "Libya (ليبيا/ Lībiyā)",
    "Liechtenstein": "Liechtenstein",
    "Lithuania": "Lithuania (Lietuva)",
    "Luxembourg": "Luxembourg",
    # M
    "Madagascar": "Madagascar (Madagasikara)",  # double check!
    "Malawi": "Malawi (Malaŵi)",
    "Malaysia": "Malaysia",
    "Maldives": "Maldives (ގުޖޭއްރާ ޔާއްރިހޫމްޖު/ Dhivehi Raajje",
    "Mali": "Mali",
    "Malta": "Malta",
    "Marshall Islands": "Marshall Islands (Aolepān Aorōkin M̧ajeļ)",  # ?, double check!
    "Mauritania": "Mauritania (موريتانيا/ Mūrītānyā)",
    "Mauritius": "Mauritius (Maurice)",
    "Mexico": "Mexico (México)",
    "Micronesia": "Micronesia",  # ?
    "Monaco": "Monaco",
    "Mongolia": "Mongolia (Монгол улс/ Mongol)",
    "Montenegro": "Montenegro (Црна Гора/ Crna Gora)",
    "Morocco": "Morocco (المغرب/ Al-Maghrib)",
    "Mozambique": "Mozambique (Moçambique)",
    "Myanmar": "Myanmar (မြန်မာ)",  # double check!
    # N
    "Namibia": "Namibia",
    "Nauru": "Nauru (Naoero)",  # double check!
    "Nepal": "Nepal (नेपाल)",
    "Netherlands": "Netherlands (Nederland)",
    "New Zealand": "New Zealand (Aotearoa)",
    "Nicaragua": "Nicaragua (Nicaragua)",
    "Niger": "Niger",
    "Nigeria": "Nigeria",
    "North Macedonia": "North Macedonia (Северна Македонија)",
    "Norway": "Norway (Norge)",
    # O, P
    "Oman": "Oman (عُمان/ Umān')",
    "Pakistan": "Pakistan (پاکستان)",
    "Palau": "Palau (Belau)",  # ?, double check!
    "Panama": "Panama",
    "Papua New Guinea": "Papua New Guinea (Papua Niugini)",  # double check!
    "Paraguay": "Paraguay",
    "Peru": "Peru (Perú)",
    "Philippines": "Philippines (Pilipinas)",  # double check!
    "Poland": "Poland (Polska)",
    "Portugal": "Portugal (Portugal)",
    # Q, R
    "Qatar": "Qatar (قطر/ Qaṭar)",
    "Republic of Korea": "Republic of Korea (한국)",
    "Republic of Moldova": "Republic of Moldova",  # double check!
    "Romania": "Romania (România)",
    "Russian Federation": "Russian Federation (Российская Федерация)",
    "Rwanda": "Rwanda",
    # S
    "Saint Kitts and Nevis": "Saint Kitts and Nevis",
    "Saint Lucia": "Saint Lucia",  # ?
    "Saint Vincent and the Grenadines": "Saint Vincent and the Grenadines",
    "Samoa": "Samoa",
    "San Marino": "San Marino",
    "Sao Tome and Principe": "São Tomé and Príncipe (São Tomé e Príncipe)",
    "Saudi Arabia": "Saudi Arabia (المملكة العربية السعودية/ As‑Su‘ūdiyya)",
    "Senegal": "Senegal (Sénégal)",
    "Serbia": "Serbia (Србија/ Srbija)",
    "Seychelles": "Seychelles (Sesel)",
    "Sierra Leone": "Sierra Leone",
    "Singapore": "Singapore (新加坡)",
    "Slovakia": "Slovakia (Slovensko)",
    "Slovenia": "Slovenia (Slovenija)",
    "Solomon Islands": "Solomon Islands",
    "Somalia": "Somalia (َلصُّومَال/ Aş Şūmāl)",
    "South Africa": "South Africa (Suid-Afrika)",
    "South Sudan": "South Sudan",
    "Spain": "Spain (España)",
    "Sri Lanka": "Sri Lanka (ශ්‍රී ලංකා/ Shrī Lamkā)",
    "Sudan": "Sudan (السودان/ As‑Sudān)",
    "Suriname": "Suriname",
    "Sweden": "Sweden (Sverige)",
    "Switzerland": "Switzerland (Schweiz/ Suisse/ Svizzera)",
    "Syrian Arab Republic": "Syrian Arab Republic (الجمهورية العربية السورية/ Sūriyā)",
    # T
    "Tajikistan": "Tajikistan (Тоҷикистон/ Tojikiston)",
    "Thailand": "Thailand (ประเทศไทย)",
    "Timor-Leste": "Timor-Leste",
    "Togo": "Togo",
    "Tonga": "Tonga",
    "Trinidad and Tobago": "Trinidad and Tobago",
    "Tunisia": "Tunisia (تونس/ Tūnis)",
    "Türkiye": "Türkiye",
    "Turkmenistan": "Turkmenistan (Türkmenistan)",
    "Tuvalu": "Tuvalu",
    # U
    "Uganda": "Uganda",
    "Ukraine": "Ukraine (Україна/ Ukraina)",
    "United Arab Emirates": "United Arab Emirates (الإمارات/ Al Imārāt)",
    "United Kingdom": "United Kingdom",
    "United Republic of Tanzania": "United Republic of Tanzania",
    "United States of America": "United States of America",
    "Uruguay": "Uruguay",
    "Uzbekistan": "Uzbekistan (O‘zbekiston)",
    # V, Y, Z
    "Vanuatu": "Vanuatu",
    "Venezuela": "Venezuela",
    "Viet Nam": "Viet Nam (Việt Nam)",
    "Yemen": "Yemen (اليَمَن/ Al Yaman)",
    "Zambia": "Zambia",
    "Zimbabwe": "Zimbabwe",
}

# territories and distant regions
overseas_terr_dict = {
    "Aruba": "Netherlands",  # integrated (non EU), caribbean
    "Azores Islands": "Portugal",  # autonomous, european islands
    "Canary Islands": "Spain",  # autonomous, north african island
    "Cook Islands": "New Zealand",  # free association, oceania
    "Curaçao": "Netherlands",  # integrated (non EU), caribbean
    "French Guiana": "France",  # fully integrated, south american mainland
    "Guadeloupe": "France",  # fully integrated, caribbean
    "Marshall Islands": "United States of America",  # freely associated, oceania
    "Martinique": "France",  # fully integrated, caribbean
    "Mayotte": "France",  # fully integrated, south-eastern african island
    "Micronesia": "United States of America",  # freely associated, oceania
    "Netherlands Antilles": "Netherlands",  # historic/ new dissolved into Curaçao, Sint Maarten, etc.
    "Niue": "New Zealand",  # free association, oceania
    "Northern Mariana Islands": "United States of America",  # unincorporated organized territory, oceania
    "Palau": "United States of America",  # free association, oceania
    "Puerto Rico": "United States of America",  # unincorporated organized territory, caribbean
    "Réunion": "France",  # fully integrated, south-eastern african island
    "Saint Barthélemy": "France",  # overseas collectivity (COM), caribbean
    "Saint Martin (French Part)": "France",  # overseas collectivity (COM), caribbean
    "Sint Maarten (Dutch part)": "Netherlands",  # integrated (non EU), caribbean
    "Wallis and Futuna Islands": "France",  # overseas collectivity (COM), oceania
}

# UN permanent observers and none states
non_un_2025_states = {
    "Palestine": "Palestine (دولة فلسطين)",  # partially recognised
    "Holy See": "Holy See (Sancta Sedes)",
    "North Korea": "North Korea (조선)",
    "Kosovo": "Kosovo (Republika e Kosovës/ Република Косово)",  # partially recognised
    "Taiwan": "Taiwan (臺灣)",  # partially recognised
}

# UN non-self-governing territories and Hong Kong and Macau
non_self_gov_2025_dict = {
    "American Samoa": "United States of America",  # unincorporated unorganized territory, caribbean, != Samoa (--> independent)
    "Anguilla": "United Kingdom",  # overseas territory, caribbean island
    "Bermuda": "United Kingdom",  # overseas territory, north american islands
    "British Virgin Islands": "United Kingdom",  # overseas territory, caribbean island
    "Cayman Islands": "United Kingdom",  # overseas territory, caribbean island
    "Falkland Islands": "United Kingdom",  # overseas territory, south american island
    "French Polynesia": "France",  # free association, oceania
    "Gibraltar": "United Kingdom",  # overseas territory, european mainland
    "Guam": "United States of America",  # unincorporated organized territory, oceania
    "Hong Kong (China)": "China",  # special administrative, china mainland
    "Macao (China)": "China",  # special administrative, china mainland
    "Montserrat": "United Kingdom",  # overseas territory, caribbean
    "New Caledonia": "France",  # special status (closer to free association), oceania
    "Pitcairn": "United Kingdom",  # overseas territory, oceania
    "Saint Helena": "United Kingdom",  # overseas territory, south-west african island
    "Tokelau": "New Zealand",  # dependend territory, oceania
    "Turks and Caicos Islands": "United Kingdom",  # overseas territory, caribbean
    "United States Virgin Islands": "United States of America",  # unincorporated organized territory, caribbean
    "Western Sahara": "Morocco"  # occupied, north africa
}

# historic labels comparable in borders and long to short UN labels
country_label_dict = {
    "Bolivia (Plurinational State of)": "Bolivia",
    "Czech Republic": "Czechia",
    "China, Hong Kong Special Administrative Region": "Hong Kong (China)",
    "China, Macao Special Administrative Region": "Macao (China)",
    "Democratic People's Republic of Korea": "North Korea",
    "German Democratic Republic": "Germany",
    "Germany Federal Republic": "Germany",
    "Iran (Islamic Republic of)": "Iran",
    "Lao People's Democratic Republic": "Lao People's D.R.",
    "Micronesia (Federated States of)": "Micronesia",
    "Netherlands (Kingdom of the)": "Netherlands",
    "People's Democratic Republic of Yemen": "Yemen",
    "Taiwan (Province of China)": "Taiwan",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "Venezuela (Bolivarian Republic of)": "Venezuela",
    "Yemen Arab Republic": "Yemen",
    "State of Palestine": "Palestine",
    "Czechoslovakia": "Czechoslovakia (historic)",
    "Netherlands Antilles": "Netherlands Antilles (historic)",
    "Serbia Montenegro": "Serbia Montenegro (historic)",
    "Soviet Union": "Soviet Union (historic)",
    "Yugoslavia": "Yugoslavia (historic)",
}

continent_list = [  # 6 regions
    "Africa",
    "Europe",  # + Russia
    "Asia",  # - Russia
    "North America",  # + Mexico, Caribbean
    "South America",  # - Mexico, Caribbean
    "Oceania",
    "International Spaces"  # Sea, Air, Space (needed?)
]

geograph_list = [  # 25 regions
    # The Americas
    "North America",  # USA, Canada, Greenland
    "Central America",  # Mexico, Guatemala, El Salvador, Honduras, Nicaragua, Costa Rica, Panama
    "Caribbean",
    "Northern South America",  # Colombia, Venezuela, Guyana, Suriname, French Guiana
    "The Amazonas",  # Brasil, Bolivia
    "The Andes",  # Chile, Peru, Ecuador
    "The Papas",  # Argentina, Paraguay, Uruguay
    # Europe
    "North-West Europe",  # Scandinavia, UK, Ireland, Benelux, Switzerland, Liechtenstein, Germany, Austria, Czechia
    "East Europe",  # Balkan States, Poland, Belarus, Slovakia, Ukraine, Hungary, Romania, Moldova, Serbia, Kosovo, North Macedonia, Russia, Georgia
    "Mediterranean",  # Portugal, Spain, Andorra, France, Italy, Slovenia, Croatia, B&H, Montenegro, Albania, Greece
    # Asia
    "The Levant & Anatolia",  # Cyprus, Syria, Lebanon, Israel, Palestine, Jordan, Turkey, Iraq
    "Arabian Peninsula & Persia",  # Arabian Peninsula, Iran, Azerbaijan, Afghanistan, Armenia, Turkmenistan
    "Southern Himalayas",  # Pakistan, India, Sri Lanka, Bangladesh, Nepal, Bhutan
    "Altai, Pamir & Tian Shan",  # Uzbekistan, Tajikistan, Kazakhstan, Kyrgyzstan, Mongolia
    "North-West Pacific (East Asia)",  # China, Taiwan, Japan, North Korea, Republic of Korea
    "South East Asia",  # Myanmar, Lao, Thailand, Cambodia, Malaysia, Viet Nam, Singapore, Indonesia, East Timor, Philippines
    # Oceania
    "Australia & New Zealand",  # Australia, New Zealand
    "Micronesia, Polynesia & Melanesia",  # Micronesia, Polynesia, Melanesia
    # Africa
    "Arab Maghreb",  # Mauritania, Western Sahara, Morocco, Algeria, Tunisia, Libya
    "Nile Basin",  # Uganda, South Sudan, Sudan, Eritrea, Egypt
    "East African Highlands",  # Djibouti, Somalia, Ethiopia, Kenya, Tanzania
    "Niger Basin & Lake Chad",  # Mali, Burkina Faso, Niger, Nigeria, Chad
    "African West Coast & Gulf of Guinea",  # CV, Senegal, The Gambia, Guinea Bissau, Guinea, Sierra Leone, Liberia, CI, Ghana, Togo, Benin, Cameroon, Eq. Guinea, STAP, Gabon, Angola
    "Congo Basin",  # Congo, D.R. of the Congo, CAR, Rwanda, Burundi
    "South African Savannas & (Semi)Deserts",  # Angola, Zambia, Malawi, Mozambique, Zimbabwe, Botswana, Namibia, South Africa, Lestho, Eswatini
    "East African Islands",  # Madagascar, Comoros, Seychelles, Mayotte, Reunion, Mauritius,
]

population_list = []  # does this make sense? change in history?

area_list = []  # does this make sense? more likely as additional dataframe...

political_list = [  # UN regions
"== to SUBREGION"
]

sovereign_list = []

country_list = []

admin_list = []
