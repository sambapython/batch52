import sqlite3
import psycopg2
def get_con():
    #con = sqlite3.connect("batch521.sqlite3")
    # install postgres, create user.
    con = psycopg2.connect(database="batch52",
    host="localhost",
    port=5432,
    user="postgres",
    password="root")
    cur=con.cursor()
    return con,cur 
def create_structure():
    con,cur=get_con()
    cur.execute("create table person(id int, name varchar(250))")
    con.commit()
    con.close()

if __name__=="__main__":
    create_structure()

