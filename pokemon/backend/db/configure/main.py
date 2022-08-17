import sys, os, pathlib, requests, json, mysql.connector

def connect(db):
    connection = mysql.connector.connect(
        host = "pokemondb.c1bl7gpkpozr.us-east-1.rds.amazonaws.com",
        user = "root",
        passwd = "Burget136!!",
        database = db
    )
    print("CONNECTED TO SERVER")
    return connection


def initialize(connection):
    with open(os.path.join(pathlib.Path().resolve(), "Scripts\initializeDB.txt"), "r") as script:
        query = script.read()

    comm.multi(connection, query)
    connection = connect("pokemondb")
    return connection
        
        
def send_query(connection, query):
    assert(query != "")
    connection.reconnect()
    query = query.split(';')
    for line in query:
        print(line)
        cursor = connection.cursor()
        cursor.execute(line)
        connection.commit()
        cursor.close()
        
def main():
    connection = connect("")
    connection = initialize(connection)
    
    
    
if __name__ == "__main__":
    main()