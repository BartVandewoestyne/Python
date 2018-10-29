import socket

s = socket.socket()
print("socket created")

s.bind(('localhost', 8000))
print("socket bound to locahost 8000")

s.listen(1)
print("socket is listening")

conn, addr = s.accept()
print("socket has accepted a connection")

while True:
    data = conn.recv(4096)
    if not data: break
    print("socket received the following data: ", repr(data))
