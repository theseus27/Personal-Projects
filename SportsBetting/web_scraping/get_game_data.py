from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()
options.add_argument("--headless=new")
driver = Chrome(options=options)

def get_season(year, url):
    url = url + str(year)
    games = []
    rows = 0
    driver.get(url)

    try:
        header_string = ".//div[@class='gamelogs-table']//div[@class='responsive-datatable__scrollable']//td[starts-with(@class, 'col-0 row-0')]"
        elts = driver.find_elements(By.XPATH, header_string)
        print(len(elts))
    except:
        return []
    
    # Get games until not found
    while True:
        try:
            search = ".//div[@class='gamelogs-table']//div[@class='responsive-datatable__scrollable']//tr[@data-index='" + str(rows) + "']"
            print(search)
            driver.get(url)
            stat = driver.find_elements(By.XPATH, search)
            games.append(stat.text)
            print(str(year) + stat)
            rows += 1
        except:
            return games


    


def get_data(player_url):
    all_years = []
    returned = [1]
    year = 2023

    while (returned != None and year > 2010):
        returned = get_season(year, player_url)

        if len(returned) == 0:
            returned = None
        else:
            all_years.append(returned)
            year -= 1
    
    print(returned)

get_data("https://www.mlb.com/player/jurickson-profar-595777?stats=gamelogs-r-hitting-mlb&year=")