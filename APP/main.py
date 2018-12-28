from dboperations import browse, insert
print("DB OPERATIONS:\n\t1.Insert\n\t2.delete\n\t3.update\n\t4.select")
opt=input("enter an option")
if opt=="4":
    c_id=input("Enter an id:")
    data =browse(c_id)
    print(data)
elif opt=="1":
    if insert():
        print("inserted successfully!!")
    else:
        print("some issue")
