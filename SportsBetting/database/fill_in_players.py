from db import connect
import pandas as pd
DATAFILE = "../data/player_links.txt"

def send_player(db, id, name, url, teamid):
    query = "INSERT INTO players(PlayerID, PlayerName, URL, TeamID) VALUES (" + str(id) + ", \'" + str(name) + "\', \'" + str(url) + "\'," + str(teamid) + ");"

    cursor = db.cursor()
    try:
        cursor.execute(query)
        db.commit()
        #print("Added " + name + " to Players")
    except:
        print("Failed to add " + name + " to Players")
    finally:
        cursor.close()


def fill_in_teams():

    # Team names to idxs
    team_file = open("../data/team_names.txt")
    teams = team_file.readlines()

    db = connect()

    infile = open(DATAFILE, 'r')
    links = infile.readlines()

    for link in links:
        name_id = link.split("/player/")[1]
        team_name = name_id.split(":::")[1]
        first_last_id = name_id.split(":::")[0].split('-')
        if team_name == "giants\n": team_name = "giants"
        team_id = teams.index(team_name)+1
        
        if (len(first_last_id) == 3):
            name = first_last_id[0] + " " + first_last_id[1]
            id = first_last_id[2]
        elif len(first_last_id) == 4:
            name = first_last_id[0] + " " + first_last_id[1] + " " + first_last_id[2]
            id = first_last_id[3]
        else:
            name = first_last_id[0] + " " + first_last_id[1] + " " + first_last_id[2] + " " + first_last_id[3]
            id = first_last_id[4]


        send_player(db, id, name, link, team_id)

fill_in_teams()