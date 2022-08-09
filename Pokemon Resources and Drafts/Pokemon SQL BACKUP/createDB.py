import sys
import os
import pathlib
import commands as comm
sys.path.append(".")

import requests                     #type:ignore
import json

def initialize(connection):
    #print(pathlib.Path().resolve())
    with open(os.path.join(pathlib.Path().resolve(), "Scripts\initializeDB.txt"), "r") as script:
        query = script.read()

    comm.multi(connection, query)
    connection = comm.connect("pokemondb")
    return connection

def populate(connection, NUM_POKEMON):
    for num in range(1, NUM_POKEMON+1):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{num}")
        data = json.loads(response.content)

        ########################################################################
        #Parse Data
        ########################################################################
        
        name = str.capitalize(data.get("species").get("name"))
        id = data.get("id")
        #imgURL = data.get("sprites").get("front_default")
        imgURL = (f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{num}.png")
        typeData = data.get("types")
        types = []
        for type in typeData:
            types.append(type.get("type").get("name"))
        if (len(types) == 1):
            types.append("none")
        
        exp = data.get("base_experience")
        statsData = data.get("stats")
        baseStats = []
        for stat in statsData:
            baseStats.append([stat.get("base_stat"), stat.get("effort")])
    
    
    
        query1 = "INSERT INTO Pokemon(name, imgURL, type1, type2) VALUES ('" + str(name) + "', '" + str(imgURL) + "', '" + str(types[0]) + "', '" + str(types[1]) + "');"
        
        print("Populating ", str(name))
        comm.multi(connection, query1)
        
        query2 = "INSERT INTO BaseStats(exp, hp, att, def, spAtt, spDef, speed, hpEV, attEV, defEV, spAttEV, spDefEV, speedEV) VALUES ( '" + str(exp) + "', '" + str(baseStats[0][0]) + "', '" + str(baseStats[1][0]) + "', '" + str(baseStats[2][0]) + "', '" + str(baseStats[3][0]) + "', '" + str(baseStats[4][0]) + "', '" + str(baseStats[5][0]) + "', '" + str(baseStats[0][1]) + "', '" + str(baseStats[1][1]) + "', '" + str(baseStats[2][1]) + "', '" + str(baseStats[3][1]) + "', '" + str(baseStats[4][1]) + "', '" + str(baseStats[5][1]) + "');"
        print("Adding stats for ", str(name), "\n")
        comm.multi(connection, query2)
