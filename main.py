import sqlite3

def sql_connection():
    try:
        con = sqlite3.connect('foodcost.db')
        print("Database is created")
    except Error:
        print(Error)
    finally:
        con.close()

sql_connection()
