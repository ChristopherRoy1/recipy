import sqlite3

def sql_connection():
    try:
        con = sqlite3.connect('foodcost.db')
        print("Database is created")
    except Error:
        print(Error)
    finally:
        con.close()

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE tbl_fooditem(id integer PRIMARY KEY, name text, description text)")

    con.commit()

def init_database():
    item_schema = "CREATE TABLE "
    vendor_schema = ""
    order_schema = ""
