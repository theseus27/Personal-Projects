from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver import Chrome, ChromeOptions
from db import connect
import pandas as pd

PLAYER_LINK_PATH = "../data/player_links.txt"
options = ChromeOptions()
options.add_argument("--headless=new")
driver = Chrome(options=options)

# Data: PlayerID, Position, Bats, Throws, Age
def write_player(db, data):
    query = "UPDATE players SET Position = \'" + data[1] + "\', Bats = \'" + data[2] + "\', Throws = \'" + data[3] + "\', Age = " + str(data[4]) + " WHERE PlayerID = " + str(data[0]) + ";"

    cursor = db.cursor()
    try:
        cursor.execute(query)
        db.commit()
        print("Updated " + str(data[0]))
    except:
        print("Failed to update " + str(data[0]))
    finally:
        cursor.close()


def get_data(link):
    data = []

    driver.get(link)
    
    list_items = driver.find_elements(By.XPATH, ".//div[@class='player-header--vitals ']//ul//li")

    for li in list_items:
        data.append(li.text)

    return data

def parse_data(data):
    if len(data) != 4:
        print("ERROR")
        print(data)
        return
    
    # Position, bats, throws, age
    new_data = [data[0]]
    handed = data[1].split(": ")[1]
    new_data.append(handed.split("/")[0])
    new_data.append(handed.split("/")[1])
    age = data[3].split(": ")[1]
    new_data.append(age)

    return new_data


def get_all_players():
    db = connect()

    with open(PLAYER_LINK_PATH, 'r') as f:
       links = f.readlines()

    for idx,val in enumerate(links):
        links[idx] = val.split(":::")[0]
        
    # Stopped on 164
    for idx,link in enumerate(links):
        if idx >= 164:
            print(idx)

            data = get_data(link)
            data = parse_data(data)

            player_id = link.split("/player/")[1].split("-")[-1]
            data.insert(0, player_id)

            write_player(db, data)

get_all_players()
driver.close()