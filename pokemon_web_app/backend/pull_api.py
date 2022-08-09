import mysql.connector  # type:ignore
import requests         # type:ignore
import json

NUM_POKEMON = 905
NUM_TYPES = 18

def pull_pokemon(connection):
    connection.reconnect()
    cursor = connection.cursor()
    query = "DELETE FROM pokemon LIMIT " + str(NUM_POKEMON) + ";"
    cursor.execute(query)
    connection.commit()
    cursor.close()
    
    for num in range(1, NUM_POKEMON+1):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{num}")
        data = json.loads(response.content)
        name = str.capitalize(data.get("species").get("name"))
        imgURL = (f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{num}.png")
        typeData = data.get("types")
        types = []
        for type in typeData:
            types.append(type.get("type").get("name"))
        if (len(types) == 1):
            types.append("")
            
        query = "INSERT INTO pokemon(id, name, imgURL, type1, type2) VALUES('" + str(num) + "', '" + str(name) + "', '" + str(imgURL) + "', '" + str(types[0]) + "', '" + str(types[1]) + "');"
       
        connection.reconnect()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()

def pull_types(connection):
    connection.reconnect()
    cursor = connection.cursor()
    query = "DELETE FROM types LIMIT " + str(NUM_TYPES) + ";"
    cursor.execute(query)
    connection.commit()
    cursor.close()
    
    for num in range(1, NUM_TYPES+1):
        response = requests.get(f"https://pokeapi.co/api/v2/type/{num}")
        data = json.loads(response.content)
        name = data.get("name")
        
        query = "INSERT INTO types(id, name) VALUES('" + str(num) + "', '" + name + "');"
        connection.reconnect()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
    

def pull_api():
    connection = mysql.connector.connect(
    host = "localhost",
    user = "pokemonappuser",
    database = "serversiderendering"
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pokemon;")
    num_db_pokemon = len(cursor.fetchall())
    cursor.close()
    
    if (num_db_pokemon < NUM_POKEMON):
        pull_pokemon(connection)
    
    connection.reconnect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM types;")
    num_db_types = len(cursor.fetchall())
    cursor.close()
    
    if (num_db_types < NUM_TYPES):
        pull_types(connection)
    