import mysql.connector  # type:ignore

def search(connection, query):
    connection.reconnect();
    
def multi(connection, query):
    print("MULTI")
    assert(query != "")
    connection.reconnect()
    query = query.split(';')
    for line in query:
        print(line)
        cursor = connection.cursor()
        cursor.execute(line)
        connection.commit()
        cursor.close()
        #output = cursor.fetchall()
        #return output

def connect(dbName):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "burgetPackard1",
        database = dbName
    )
    print("CONNECTED TO SERVER")
    return connection
        

