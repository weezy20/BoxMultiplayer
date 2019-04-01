import socket
import _thread
import sys

server = ""
port = 10000 #randomly chosen
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind port and socket to server
try:
    s.bind((server, port))
except socket.error as e:
    str(e)
s.listen(2) #for 2 people, optional,
print("Waiting for a connection, Server started. . . ")

def threaded_client(conn):
    pass


while True:
    conn , addr = s.accept()
    print ("Connected to : ", addr)
