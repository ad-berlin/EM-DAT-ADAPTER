# basic constants col names EM-DAT
YEAR_START = 'Start Year'
MONTH_START = 'Start Month'
DAY_START = 'Start Day'
YEAR_END = 'End Year'
MONTH_END = 'End Month'
DAY_END = 'End Day'

COUNTRY = 'Country'
REGION = 'Region'
SUBREGION = 'Subregion'
LOCATION = 'Location'
RIVER = 'River Basin'
NUM = 'DisNo.'
DIS_NAT_TECH = 'Disaster Group'
DIS_SUBGROUP = 'Disaster Subgroup'
DIS_TYPE = 'Disaster Type'
DIS_SUBTYPE = 'Disaster Subtype'

ORIGIN = "Origin"
ASS_TYPES = "Associated Types"

AID = "AID Contribution ('000 US$)"
RECONSTRUCTION = "Reconstruction Costs ('000 US$)"
RECONSTRUCTION_ADJ = "Reconstruction Costs, Adjusted ('000 US$)"
INSURED = "Insured Damage ('000 US$)"
INSURED_ADJ = "Insured Damage, Adjusted ('000 US$)"
DAMAGE = "Total Damage ('000 US$)"
DAMAGE_ADJ = "Total Damage, Adjusted ('000 US$)"

MAG = "Magnitude"
MAG_SCALE = "Magnitude Scale"

DEATHS = 'Total Deaths'
INJURED = 'No. Injured'
AFFECTED = 'No. Affected'
HOMELESS = 'No. Homeless'
TOT_AFFECTED = 'Total Affected'

HIST = "Historic"
CLASS_KEY = "Classification Key"
EXT_ID = "External IDs"
NAME = "Event Name"
ISO = "ISO"  # alpha 3 for country ISO 3166 norm
OFDA_BHA = "OFDA/BHA Response"
INTERNAT_ASSIST_REQ = "Appeal"
EM_DECLARE = "Declaration"
LAT = "Latitude"
LONG = "Longitude"
CPI = "CPI"
ADMIN_UNITS = "Admin Units"

ENTRY_DATE = "Entry Date"
UPDATE_DATE = "Last Update"

# - - - - - - - - - - -
# additional col names after get_data(file)
DATE_START = "Start Date"
DATE_END = "End Date"
DIS_DURATION = "Duration of Disaster"

CONTINENT_R = 'Continent'
M49_CODE_R = 'M49 Region Code'
GEOGRAPH_SR = 'Geographic Subregion'
M49_CODE_SR = 'M49 Subregion Code'
UN_M49_IR = 'M49 Intermediate Region'
M49_CODE_IR = 'M49 Intermediate Region Code'
SOVEREIGN_C = 'UN Sovereign State'
ADMIN_C = 'Administrative Region'
UN_M49_C = 'M49 Country/Area'
M49_CODE_C = 'M49 Country/Area Code'
ISO_A2 = 'ISO-alpha2 Code'
ISO_A3 = 'ISO-alpha3 Code'

ORIGIN_CLEAN = 'Origin (clean)'
ORIGIN_LABEL = 'Origin (label)'

# - - - - - - - - - - -
# constants for layout
COLOR_NUM_PLOT = "#c71585"  # "#8e3a59"

# - - - - - - - - - - -
# additional constants
NUMBER_EV = "Number of Events"

# - - - - - - - - - - -
# lists of constants
original_list = [NUM, DIS_NAT_TECH, DIS_SUBGROUP, DIS_TYPE, DIS_SUBTYPE, COUNTRY, REGION, SUBREGION, LOCATION, ORIGIN,
                 YEAR_START, MONTH_START, DAY_START, YEAR_END, MONTH_END, DAY_END, MAG, MAG_SCALE, DEATHS, INJURED,
                 AFFECTED, HOMELESS, TOT_AFFECTED, RIVER, ASS_TYPES, AID, RECONSTRUCTION, RECONSTRUCTION_ADJ, INSURED,
                 INSURED_ADJ, DAMAGE, DAMAGE_ADJ, UPDATE_DATE, ENTRY_DATE, ADMIN_UNITS, CPI, LONG, LAT, EM_DECLARE,
                 INTERNAT_ASSIST_REQ, OFDA_BHA, ISO, NAME, EXT_ID, CLASS_KEY, HIST]

new_list = [DATE_START, DATE_END, DIS_DURATION, CONTINENT_R, M49_CODE_R, GEOGRAPH_SR, M49_CODE_SR, UN_M49_IR,
            M49_CODE_IR, SOVEREIGN_C, ADMIN_C, UN_M49_C, M49_CODE_C, ISO_A2, ISO_A3]

int_list = [INJURED, AFFECTED, HOMELESS, DEATHS, TOT_AFFECTED, RECONSTRUCTION_ADJ, INSURED,
            INSURED_ADJ, DAMAGE, DAMAGE_ADJ, DIS_DURATION, MAG]

info_list = [ORIGIN, ASS_TYPES, REGION, SUBREGION, LOCATION, RIVER, MONTH_START, CONTINENT_R, SUBREGION, UN_M49_IR,
             NAME]

att_list = [DIS_SUBGROUP, DIS_TYPE, DIS_SUBTYPE, CLASS_KEY]

plot_list = [INJURED, AFFECTED, HOMELESS, DEATHS, TOT_AFFECTED, MAG, RIVER, ASS_TYPES, RECONSTRUCTION,
             RECONSTRUCTION_ADJ, INSURED, INSURED_ADJ, DAMAGE, DAMAGE_ADJ, DIS_SUBGROUP,
             DIS_TYPE, DIS_SUBTYPE, CLASS_KEY, REGION, SUBREGION, CONTINENT_R, UN_M49_IR, LOCATION, MONTH_START]

overview_list = [INJURED, AFFECTED, HOMELESS, DEATHS, TOT_AFFECTED, RECONSTRUCTION_ADJ, INSURED,
                 INSURED_ADJ, DAMAGE, DAMAGE_ADJ, DIS_DURATION, NUMBER_EV]
