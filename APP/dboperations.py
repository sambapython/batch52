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
    q="insert into person(id,name) values(%s,'%s')"%(c_id,name)
    con,cur=get_con()
    cur.execute(q)
    con.commit()
    return browse(c_id)
def update():
    c_id=input("Enter id to update:")
    if c_id:
        old_data = browse(c_id)
        print(old_data)
        opt=input("Do you want to update(y/n):")
        if opt.lower()=="y":
            new_name=input("Enter new name:")
            q="update person set name='%s' where id=%s"%(new_name,c_id)
            con,cur=get_con()
            cur.execute(q)
            con.commit()
            con.close()
        else:
            print("thank you")
            return False
    else:
        print("expecting a prorper id")
        return False
    return True
def delete():
    c_id=input("Enter id to delete:")
    if c_id:
        old_data = browse(c_id)
        print(old_data)
        opt=input("Do you want to delete(y/n):")
        if opt.lower()=="y":
            q="delete from person where id=%s"%c_id
            con,cur=get_con()
            cur.execute(q)
            con.commit()
            con.close()
        else:
            print("thank you")
            return False
    else:
        print("expecting a prorper id")
        return False 
    return True

