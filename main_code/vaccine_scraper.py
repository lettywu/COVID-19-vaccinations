# Import libaries here
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep, time

# initialize what site we want to scrape
home_url = 'https://covid.cdc.gov/covid-data-tracker/#vaccinations'
browser = webdriver.Chrome(ChromeDriverManager().install())

# open browser and get html code 
browser.get(home_url)
sleep(3)
html = browser.page_source

home_soup = BeautifulSoup(html, 'lxml')

# close browser
browser.close()
browser.quit()

states = home_soup.find_all('tr')

# put the info we need in a dictionary
states_info = []
no_header = states[1:]
ind_state_info = [{'state': j.find_all('td')[0].text, 'total_doses_distributed': j.find_all('td')[1].text,
                      'total_doses_administered': j.find_all('td')[2].text, 'doses_distributed_100k': j.find_all('td')[3].text,
                       'doses_administed_100k': j.find_all('td')[4].text, 'people_1+_dose': j.find_all('td')[5].text,
                       'doses_1+_100k': j.find_all('td')[6].text, 'people_2_doses': j.find_all('td')[7].text,
                       'doses_2_100k': j.find_all('td')[7].text} for j in no_header]
states_info += ind_state_info

# save our important info to dataframe and save as csv
final_info = pd.DataFrame(states_info)
final_info.to_csv(f'../data/vaccinations_{int(time())}.csv', index = False)
