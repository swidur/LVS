import sqlite3 as lite
from connector import Connector


def database(path= 'default.db'):
    try:
        con = Connector(path).connect()

        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS brands(brand_id INTEGER PRIMARY KEY,name TEXT NOT NULL)")

        cur.execute("CREATE TABLE IF NOT EXISTS t_types(type_id INTEGER PRIMARY KEY NOT NULL,name text NOT NULL)")

        cur.execute("CREATE TABLE IF NOT EXISTS storagespaces(storage_id INTEGER PRIMARY KEY, stillage TEXT NOT NULL,x INTEGER NOT NULL CHECK (x > 0),y INTEGER NOT NULL CHECK (y > 0))")

        cur.execute("CREATE TABLE IF NOT EXISTS wheel(wheel_id INTEGER PRIMARY KEY,width INTEGER NOT NULL CHECK(width > 0),height INTEGER NOT NULL CHECK(height > 0),inches DOUBLE NOT NULL CHECK(inches > 0),t_depth DOUBLE,t_type INTEGER NOT NULL,brand INTEGER NOT NULL,dot INTEGER NOT NULL,storage_space_id INTEGER NOT NULL)")
        con.commit()
    except lite.Error, e:

        print "Error %s:" % e.args[0]
