import socket
from _thread import *
import sys

server = "192.168.0.100"
port = 10000 #randomly chosen
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind port and socket to server
try:
    s.bind((server, port))
except socket.error as e:
    str(e)
s.listen(2) #for 2 people, optional,
#if left blank, listens for unlimited connections

print("Waiting for a connection, Server started. . . ")

def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply=""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            if not data:
                print("Disconnected . . .")
                break
            else:
                print("Recieved : ", reply)
                print("Sending: ", reply)
            conn.sendall(str.encode(reply))
        except:
            break



while True:
    conn , addr = s.accept()
    print ("Connected to : ", addr)
    start_new_thread(threaded_client, (conn,))
