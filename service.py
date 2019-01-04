"""
host,port
form a url for service: binding
wait for client request: listen
once the client send a request need to accept that: accept
send
recv
"""
import socket
#print(socket.gethostname())
hostname=socket.gethostname()
port=8081
s=socket.socket()
s.bind((hostname,port))
 # 25->1 20 are in browsing, 4 people will get server not reachable
try:
	while True:
		s.listen(20)
		print("service running in: %s:%s"%(hostname, port))
		#print(s.accept())
		client_sock, client_info = s.accept()
		client_sock.send(b"Hello firefox how are you??")
		number = client_sock.recv(10)
		resp= b"EVEN" if int(number)%2==0 else b"ODD"
		client_sock.send(resp)
except Exception as err:
	print(err)
finally:
	s.close()
