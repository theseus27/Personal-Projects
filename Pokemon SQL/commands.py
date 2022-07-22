import mysql.connector  # type:ignore

def single(connection, query):
    connection.reconnect()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()

def multi(connection, query):
    connection.reconnect()
    query = query.split(';')
    for line in query:
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
        

