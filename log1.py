import logging
logging.basicConfig(filename="log.txt",level=logging.DEBUG,
    format="%(asctime)s->%(filename)s>%(levelname)s->%(message)s")
# info, warn, error, debug
print("welcome")
logging.info("program execution started")
a=input("Enter a number:")
logging.debug("a value give:%s"%a)
b=input("Enter b number:")
logging.debug("b value give:%s"%b)
logging.debug("before conversion a=%s, b=%s"%(a,b))
try:
    a=float(a)
    logging.info("a conversion completed.")
    b=float(b)
    logging.info("b conversion completed.")
    logging.debug ("after conversion a=%s, b=%s"%(a,b))
    res=a/b
    print("res=%s"%res)
    logging.debug("res=%s"%res)
except ZeroDivisionError:
    logging.error("expecting >0 value for b")
    print("expecting >0 value for b")
except ZeroDivisionError:
    logging.error("expecting >0 value for b")
    print("expecting >0 value for b")
except ValueError:
    logging.error("expectiong only digits")
    print("expectiong only digits")
except Exception as err:
    logging.error("%s"%err)
    print("ERROR:",err)
    print("something went wrong!!")
except:
    logging.error("some system exceptions!!")
    print("some system exceptions!!")
print("thank you!!")
logging.info("program exection completed")