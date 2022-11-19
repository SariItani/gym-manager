import sqlite3 as sq

def readData():
    connection = sq.connect('db.sqlite3')
    cursor  = connection.cursor()
    