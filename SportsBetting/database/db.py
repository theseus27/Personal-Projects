import mysql.connector
import os

def connect():
    db = mysql.connector.connect(user='Theseus', password='136###Vault',
                                        host='127.0.0.1', database='baseball')
    if not db.is_connected():
        print("Error connecting to SQL")
        return
    else:
        print("DB Connected")
        return db
    
def post(db, cmd):
    cursor = db.cursor()
    result = cursor.execute(cmd)

def get(db, cmd):
    cursor = db.cursor()
    cursor.execute(cmd)

    results = []
    for item in cursor:
        results.append(item)
    
    cursor.close()
    return results