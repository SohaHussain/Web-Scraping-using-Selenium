from selenium import webdriver

website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = 'C:/Users/sohal/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)

# <---------   FOR CLICKING A BUTTON    ------------>

# XPath Syntax
# //tag name[@AttributeName="Value"]

all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()


# <---------   EXTRACTING DATA FROM TABLE   ---------->

matches = driver.find_elements_by_tag_name('tr')  # tr is for table row , returns a list

# use find_element_by_tag_name to get only single element of the particular tag name

# empty lists to store data
date = []
home_team = []
score = []
away_team = []

for match in matches:
#   print(match.text)
    date.append(match.find_element_by_xpath('./td[1]').text) # . if for reference .ie. tr
                                                             # indexing for xpath starts from 1
    home_team.append(match.find_element_by_xpath('./td[2]').text)
    score.append(match.find_element_by_xpath('./td[3]').text)
    away_team.append(match.find_element_by_xpath('./td[4]').text)

driver.quit() # to close the website window


# <----------- EXPORTING DATA TO CSV FILE ------------->

import pandas as pd

# creating a dataframe from dictionaries
df = pd.DataFrame({'Data': date, 'Home Team': home_team, 'Score': score, 'Away Team': away_team})

# exporting data to csv file
df.to_csv('FootBall_Data.csv', index = False)

print(df)


# <---------- SELECTING ELEMENTS WITHIN A DROPDOWN FOR DYNAMIC WEBSITES ------------->

from selenium.webdriver.support.ui import Select
import time

dropdown = Select(driver.find_element_by_id('country'))
dropdown.select_by_visible_text('Spain')
time.sleep(3) # stopping the code for 3 seconds for the page to load and execute the next line of code









