# basic variables
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
# variables after get_data(file)
DATE_START = "Start Date"
DATE_END = "End Date"
DIS_DURATION = "Duration of Disaster"

# - - - - - - - - - - -
# lists of variables
bar_list = [INJURED, AFFECTED, HOMELESS]

info_list = [ORIGIN, MAG, RIVER, ASS_TYPES]

money_list = [AID, RECONSTRUCTION, RECONSTRUCTION_ADJ, INSURED, INSURED_ADJ, DAMAGE, DAMAGE_ADJ]

plot_list = [INJURED, AFFECTED, HOMELESS, ORIGIN, MAG, RIVER, ASS_TYPES, AID, RECONSTRUCTION,
             RECONSTRUCTION_ADJ, INSURED, INSURED_ADJ, DAMAGE, DAMAGE_ADJ]


# for copy and paste
full_var_basic_list = [
    YEAR_START, MONTH_START, DAY_START, YEAR_END, MONTH_END, DAY_END, COUNTRY, REGION, SUBREGION,
    LOCATION, RIVER, NUM, DIS_NAT_TECH, DIS_SUBGROUP, DIS_TYPE, DIS_SUBTYPE, ORIGIN, ASS_TYPES, AID,
    RECONSTRUCTION, RECONSTRUCTION_ADJ, INSURED, INSURED_ADJ, DAMAGE, DAMAGE_ADJ, MAG, MAG_SCALE,
    DEATHS, INJURED, AFFECTED, HOMELESS,
]

# for copy and paste
full_var_list = [
    YEAR_START, MONTH_START, DAY_START, YEAR_END, MONTH_END, DAY_END, COUNTRY, REGION, SUBREGION,
    LOCATION, RIVER, NUM, DIS_NAT_TECH, DIS_SUBGROUP, DIS_TYPE, DIS_SUBTYPE, ORIGIN, ASS_TYPES, AID,
    RECONSTRUCTION, RECONSTRUCTION_ADJ, INSURED, INSURED_ADJ, DAMAGE, DAMAGE_ADJ, MAG, MAG_SCALE,
    DEATHS, INJURED, AFFECTED, HOMELESS, DATE_START, DATE_END, DIS_DURATION,
]

