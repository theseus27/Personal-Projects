import sys
import os
import pathlib
import commands as comm
sys.path.append(".")

import requests                     #type:ignore
import json

def initialize(connection):
    #print(pathlib.Path().resolve())
    with open(os.path.join(pathlib.Path().resolve(), "Scripts\initializeTable.txt"), "r") as script:
        query = script.read()

    comm.multi(connection, query)
    connection = comm.connect("pokemon")
    return connection

def populate(connection, NUM_POKEMON):
    for num in range(1, NUM_POKEMON+1):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{num}")
        data = json.loads(response.content)

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
        if (exp == None):
            exp = 0;
        
        statsData = data.get("stats")
        baseStats = []
        for stat in statsData:
            baseStats.append([stat.get("base_stat"), stat.get("effort")])
    
        query = "INSERT INTO pokedex(Name, PokedexNumber, imgURL, Type1, Type2, BaseEXP, BaseHP, BaseAtt, BaseDef, BaseSpAtt, BaseSpDef, BaseSp) VALUES ('" + str(name) + "', '" + str(id) + "', '" + str(imgURL) + "', '" + str(types[0]) + "', '" + str(types[1]) + "', '" + str(exp) + "', '" + str(baseStats[0][0]) + "', '" + str(baseStats[1][0]) + "', '" + str(baseStats[2][0]) + "', '" + str(baseStats[3][0]) + "', '" + str(baseStats[4][0]) + "', '" + str(baseStats[5][0]) + "');"
        
        print("Populating ", str(name))
        comm.multi(connection, query)
