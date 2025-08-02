# basic constants col names
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
HOMELESS = "No. Homeless"

# - - - - - - - - - - -
# additional col names after get_data(file)
DATE_START = "Start Date"
DATE_END = "End Date"
DIS_DURATION = "Duration of Disaster"
CONTINENT = 'Continents'
UN_M49_R = 'UN M49 Regions'
GEOGRAPH_R = 'Geographical Regions'
UN_M49_SUBR = 'UN M49 Subregions'
SOVEREIGN_C = 'UN Sovereign Countries'
ADMIN_C = 'Administrative Regions'
UN_M49_C = 'UN M49 Countries'

# - - - - - - - - - - -
# constants for layout
COLOR_NUM_PLOT = "#c71585"  # "#8e3a59"

# - - - - - - - - - - -
# additional constants
NUMBER_EV = "Number of Events"

# - - - - - - - - - - -
# lists of constants
int_list = [INJURED, AFFECTED, HOMELESS, DEATHS, AID, RECONSTRUCTION, RECONSTRUCTION_ADJ, INSURED,
            INSURED_ADJ, DAMAGE, DAMAGE_ADJ, DIS_DURATION, MAG]

info_list = [ORIGIN, ASS_TYPES, REGION, SUBREGION, LOCATION, RIVER, MONTH_START]

att_list = [DIS_SUBGROUP, DIS_TYPE, DIS_SUBTYPE]

plot_list = [INJURED, AFFECTED, HOMELESS, DEATHS, ORIGIN, MAG, RIVER, ASS_TYPES, AID, RECONSTRUCTION,
             RECONSTRUCTION_ADJ, INSURED, INSURED_ADJ, DAMAGE, DAMAGE_ADJ, DIS_SUBGROUP,
             DIS_TYPE, DIS_SUBTYPE, REGION, SUBREGION, DIS_DURATION, LOCATION, MONTH_START]

overview_list = [INJURED, AFFECTED, HOMELESS, DEATHS, AID, RECONSTRUCTION, RECONSTRUCTION_ADJ, INSURED,
                 INSURED_ADJ, DAMAGE, DAMAGE_ADJ, DIS_DURATION, NUMBER_EV]
