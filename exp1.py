print("welcome")
a=input("Enter a number:")
b=input("Enter b number:")
from time import sleep
print ("before conversion a=%s, b=%s"%(a,b))
try:
    a=float(a)
    b=float(b)
    sleep(10)
    print ("after conversion a=%s, b=%s"%(a,b))
    res=a/b
    print("res=%s"%res)
except ZeroDivisionError:
    print("expecting >0 value for b")
except ZeroDivisionError:
    print("expecting >0 value for b")
except ValueError:
    print("expectiong only digits")
except Exception as err:
    print("ERROR:",err)
    print("something went wrong!!")
except:
    print("some system error!!!")

print("thank you!!")