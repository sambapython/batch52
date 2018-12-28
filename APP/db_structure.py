import sqlite3
def get_con():
    con = sqlite3.connect("batch521.sqlite3")
    cur=con.cursor()
    return con,cur 
def create_structure():
    con,cur=get_con()
    cur.execute("create table person(id int, name varchar(250))")
    con.commit()
    con.close()
if __name__=="__main__":
    create_structure()

