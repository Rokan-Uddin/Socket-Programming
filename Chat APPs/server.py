import socket
import sys
import time

s=socket.socket()
host= socket.gethostname()
port=8080
print("Hostname:",host)
s.bind((host,port))
s.listen(1)
conn,addr=s.accept()
while 1:
    message=input(str(">>>>"))
    message=message.encode()
    conn.send(message)
    print("")
    incoming_message =conn.recv(1024)
    incoming_message =incoming_message.decode()
    print("Client:", incoming_message)
    print("")
