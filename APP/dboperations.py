from db_structure import get_con
def browse(c_id=None):
    con,cur=get_con()
    if c_id:
        q="select * from person where id=%s"%c_id
    else:
        q="select * from person"
    cur.execute(q)
    data=cur.fetchall()
    con.close()
    return data
def insert():
    c_id=input("Enter customer id:")
    name=input("Enter name:")
    q="insert into customer(id,name) values(%s,'%s')"%(c_id,name)
    con,cur=get_con()
    cur.execute(q)
    con.commit()
    return browse(c_id)
