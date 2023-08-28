from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()
options.add_argument("--headless=new")
driver = Chrome(options=options)

def get_data_dimensions(year, url):
    rows = 0
    cols = 0
    cont = True
    driver.get(url)

    # Check for header
    header_string = ".//div[@class='responsive-data__scrollable']//td[starts-with(@class, 'col-0 row-0')]"
    try:
        stat = driver.find_elements(By.XPATH, header_string)
        print(stat)
        if len(stat) == 0:
            cont = False
    except:
        return [0, 0]

    # Get number of rows
    while cont:
        try:
            search_string = ".//div[@class='responsive-data__scrollable']//td[starts-with(@class, 'col-0 row-" + str(rows) + "')]"

            row = driver.find_elements(By.XPATH, search_string)
            if len(row) == 0:
                cont = False
            else:
                rows += 1
            print(rows)
        except Exception as e:
            print("Row exception on row = " + str(rows))
            cont = False
        
    if rows > 0:
        cont = True
    
    while cont:
        try:
            search_string = ".//div[@class='responsive-data__scrollable']//td[starts-with(@class, 'col-" + str(cols) + " row-0')]"
            driver.find_elements(By.XPATH, search_string)
            print(search_string)
            cols += 1
        except:
            print("Col exception on col = " + str(cols))
            cont = False
    
    return [rows, cols]


def get_season(year, url):
    url += str(year)

    dims = get_data_dimensions(year, url)
    print(dims)
    rows = dims[0]
    cols = dims[1]

    # game_data = [[None for i in range(cols)] for i in range(rows)]

    # driver.get(url)

    # for i in rows:
    #     for j in cols:
    #         search_string = ".//div[@class='responsive-data__scrollable']//tr[@data_index=" + str(i) + "//td[@data_col=" + str(j) + "]"
    #         stat = driver.find_element(By.XPATH, search_string)
    #         game_data[i][j] = stat.text

    # return game_data

    if rows > 0 and cols > 0:
        return [rows, cols]
    else:
        return []


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

#get_data("https://www.mlb.com/player/jurickson-profar-595777?stats=gamelogs-r-hitting-mlb&year=")

driver.get("https://www.mlb.com/player/jurickson-profar-595777?stats=gamelogs-r-hitting-mlb&year=2023")
header_string = ".//div[@class='gamelogs-table']//div[@class='responsive-datatable__scrollable']//td[starts-with(@class, 'col-0 row-0')]"

header_string = ".//div[@class='gamelogs-table']//div[@class='responsive-datatable__scrollable']//tr[@data-index='0']"

idx = 0
header_string = ".//div[@class='gamelogs-table']//div[@class='responsive-datatable__scrollable']//tr[@data-index='" + str(idx) + "']"
stat = driver.find_elements(By.XPATH, header_string)
print(len(stat))
for s in stat:
    print(s.text)

driver.close()