# Import Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# Connecting to site
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

with open('../Input/URL.txt', 'r') as input_data:
    for line in input_data:
        url = line

with open('../Input/Champions List.txt', 'r') as input_data:
    all_champs = [line.strip() for line in input_data]

browser.visit(url)

matches_ls = []

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

champ_rows = soup.find_all('div', class_='row champion-table__row')

for item in all_champs:
    for champ in champ_rows:
        if champ.find('div', class_='row__champion__name').text == item:
           print(champ.find_all('div', class_='percentile-stat__value c-help col-11'))

#browser.links.find_by_partial_text('Next').click()

# browser.quit()