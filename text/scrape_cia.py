from worldfactbook import WorldFactbook
import streamlit as st

# https://github.com/lucafrance/cia-factbook-scraper/blob/main/cia_factbook_scaper.py

factbook = WorldFactbook(cache_folder="cache", use_cache=True)

# Get population data
populations = factbook.get_populations()
st.write(populations)

# Get language distribution
languages = factbook.get_languages()
st.write(languages)

# Get country ISO codes
country_codes = factbook.get_country_codes()
st.write(country_codes)

# Lower-level API calls
country_comparison_data = factbook.get_field_country_comparison_data("population")  # Get population comparison data
st.write(country_comparison_data)
field_data = factbook.get_field_data("languages")  # Get field data like languages
st.write(field_data)
reference_data = factbook.get_reference_data("country-data-codes")  # Get reference data for country codes
st.write(reference_data)
