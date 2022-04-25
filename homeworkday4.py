import requests
from selenium import webdriver
from selenim.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep

driver = webdriver.Chrome('./chromedriver')
# response = requests.get('https://modest-jennings-77f32e.netlify.app/login')
print(response.content)

driver.get('https://modest-jennings-77f32e.netlify.app/login')

sleep(4)
oldest_players = {
    "Atl": "Lou Williams",
    "Bos": "Tristan Thompson",
    # Etc for all teams
}