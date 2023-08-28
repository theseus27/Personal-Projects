from db import connect

def read_players():
    db = connect()
    query = "SELECT * FROM players"

    cursor = db.cursor()
    try:
        results = cursor.execute(query)
        print("Read " + str(len(results)) + " players")
    except:
        print("Failed to read players")
    finally:
        cursor.close()

read_players()