import requests
import streamlit as st
from bs4 import BeautifulSoup

def test123():
    url = "https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/"
    response = requests.get(url)
    print(response.text)

def soup():
    # Fetch and parse the page
    response = requests.get('https://www.cia.gov/the-world-factbook/countries/afghanistan/')
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the main content container
    content_div = soup.find('<div', class_='article--viewer_content')
    if content_div:
        for para in content_div.find_all('p'):
            print(para.text.strip())
    else:
        print("No article content found.")

test123()
soup()