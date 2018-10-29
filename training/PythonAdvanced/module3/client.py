# TODO: dit was nog niet klaar
import socket

s = socket.socket()
s.connect('localhost', 8000)
s.send(b'Hello')