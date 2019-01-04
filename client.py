import socket
s=socket.socket()
hostname="khyaathipython"
port=8081
s.connect((hostname,port))
ack=s.recv(1024)
print(ack)
number = input("enter a numbe:")
s.send(str.encode(number))
res = s.recv(1024)
print("result=",res)
s.close()