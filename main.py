import sqlite3

def create_food_item_table():
    item_schema = "CREATE TABLE tbl_item(
                        item_id integer PRIMARY KEY,
                        name text,
                        unit text,
                        base_quantity real,
                        description text)"

def create_vendor_table():
    vendor_schema = "CREATE TABLE tbl_vendor(
                    vendor_id integer PRIMARY KEY,
                    name text,
                    creation_date TEXT)"

def create_food_order_table():
    food_order_schema = "CREATE TABLE tbl_order(
                        order_id INTEGER PRIMARY KEY,
                        order_date TEXT,
                        vendor_id INTEGER NOT NULL,
                        FOREIGN KEY (vendor_id) REFERENCES tbl_vendor(vendor_id)"

def create_food_order_item_table():
    food_order_item_schema = "CREATE TABLE tbl_order_item(
                              id INTEGER PRIMARY KEY,
                              order_id INTEGER,
                              item_id INTEGER,
                              FOREIGN KEY (order_id) REFERENCES tbl_order(order_id),
                              FOREIGN KEY (item_id)  REFERENCES tbl_item(item_id)
    )"

def create_recipe_table():
    recipe_schema = "CREATE TABLE tbl_recipe(
                     recipe_id INTEGER PRIMARY KEY,
                     name TEXT,
                     creation_date TEXT,
                     last_modified TEXT,
    )"

def create_recipe_item_table():
    recipe_item_schema = "CREATE TABLE tbl_recipe_item(
                         recipe_item_id INTEGER PRIMARY KEY,
                         recipe_id INTEGER,
                         item_id INTEGER,
                         FOREIGN KEY (item_id)  REFERENCES tbl_item(item_id),
                          FOREIGN KEY (recipe_id)  REFERENCES tbl_recipe(recipe_id)
    )"


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
    cursorObj.execute()

    con.commit()

def init_database():
    create_food_item_schema()
    create_vendor_table()
    create_food_order_table()
