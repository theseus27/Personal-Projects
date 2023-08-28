from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver import Chrome, ChromeOptions
TEAM_LIST_PATH = "../data/team_names.txt"
LINK_OUTPUT_PATH = "../data/player_links.txt"

options = ChromeOptions()
options.add_argument("--headless=new")
driver = Chrome(options=options)

def get_roster_of_team(team):
    URL = "https://www.mlb.com/" + team + "/roster/40-man"

    driver.get(URL)
    link_data = driver.find_elements(By.XPATH, ".//a[contains(@href,'player/')]")
    links = []

    for link in link_data:
        links.append(link.get_attribute("href") + ":::" + team)

    return links

def get_all_teams():
    with open(TEAM_LIST_PATH, 'r') as f:
        teams = f.readlines()

    urls = []
    for team in teams:
        team_urls = get_roster_of_team(team)
        for url in team_urls:
            urls.append(url)

    print(len(urls))
    
    with open(LINK_OUTPUT_PATH, 'w') as outfile:
        for url in urls:
            outfile.write(url)

get_all_teams()
driver.close()