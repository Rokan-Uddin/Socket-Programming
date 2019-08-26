import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
s.listen(2)
print(host)
print("Waiting for any incoming connections ... ")
for x in range (2):
    conn, addr = s.accept()
    print(addr, "Has connected to the server")

    filename = input(str("Please enter the filename of the file : "))
    file = open(filename , 'rb')
    file_data = file.read(400000000)
    conn.send(file_data)
    print("Data has been transmitted successfully")

