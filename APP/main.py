from dboperations import browse, insert, update, delete
while True:
    print("DB OPERATIONS:\n\t1.Insert\n\t2.delete\n\t3.update\n\t4.select\
\n\tq.quit")
    opt=input("enter an option")
    if opt.lower()=="q" or opt.lower() == "quit":
        break
    elif opt=="4":
        c_id=input("Enter an id:")
        data =browse(c_id)
        print(data)
    elif opt=="1":
        if insert():
            print("inserte successfully!!")
        else:
            print("some issue")
    elif opt=="3":
        if update():
            print("updated successfully")
        else:
            print("updation not done")
    elif opt=="2":
        if delete():
            print("deleted successfully")
        else:
            print("deletion not done")
