import socket

HOST, PORT = "127.0.0.1", 8888

socket_a = socket.socket()
socket_a.bind((HOST, PORT))
socket_a.listen(5)
conn, add = socket_a.accept()
print conn, add
while True:
    data = conn.recv(1024)
    print data
    if not data:
        print "End recv"
        break

conn.close()