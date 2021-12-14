from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re
from selenium.webdriver.common.keys import Keys
import os


options = Options()
# options.add_argument("--start-maximized")
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)

table = {}

def getData():
    url="https://www.trustpilot.com"
    driver.get(url)
    searchInput = driver.find_element(By.CSS_SELECTOR, "#heroSearchContainer > div > div > div > div > form > input").send_keys("DailySale.com")
    searchClick = driver.find_element(By.CSS_SELECTOR, "#heroSearchContainer > div > div > div > div > form > div.searchButtonDesktop___3iJZC > button").click()
    reviewBox = driver.find_elements(By.CSS_SELECTOR, "#__next > div > main > div > div.styles_mainContent__nFxAv > section > div > article")
    print(len(reviewBox))
    for i in reviewBox:
        try:
            rate = i.find_element(By.CSS_SELECTOR, 'div.star-rating_starRating__4rrcf.star-rating_medium__iN6Ty > img').get_attribute('alt')
            print(rate[6])
        except:
            rate = ""
        try:
            title = i.find_element(By.CSS_SELECTOR, 'div.styles_reviewContent__9_S10 > h2 > a').get_attribute("innerText")
            print(title)
        except:
            title = ""
            print("no title")
        try:
            reviewText = i.find_element(By.CSS_SELECTOR, 'div.styles_reviewContent__9_S10 > p').get_attribute("innerText")
            print(reviewText)
        except:
            reviewText = ""
            print("no review")

getData()
driver.close()


