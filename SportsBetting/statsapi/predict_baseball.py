import requests
import json
import statsapi

def predict_winner():

    url = "http://lookup-service-prod.mlb.com/json/named.team_all_season.bam?"

    headers = {
        "Content-Type" : "application/json"
    }

    params = {"sport_code":'mlb',"all_star_sw":"N","sort_order":"name_asc","season":"2023"}


    response = requests.get(url, headers=headers, params=params)

    print(response.text)

#predict_winner()

rook_hr_lead = statsapi.league_leaders('homeRuns', season=2023, playerPool='rookies', limit=5)
rook_hr_leaders = rook_hr_lead.split('\n')
#print(rook_hr_leaders)

game_data = statsapi.boxscore_data(565997)
game_data = str(game_data)

f = open('gameoutput.txt', 'w')
f.write(game_data)