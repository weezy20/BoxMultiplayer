import socket
from _thread import *
import sys

server = "192.168.0.101"
port = 10000 #randomly chosen
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind port and socket to server
try:
    s.bind((server, port))
except socket.error as e:
    str(e)
s.listen(2)
#opens port for 2 people, args optional,
#if left blank, listens for unlimited connections
print("Waiting for a connection, Server started. . . ")

def read_pos(str):
    str = str.split(',')
    return int(str[0]), int(str[1])

def make_pos(tuple):
    return str(tuple[0]) + ',' + str(tuple[1])

def threaded_client(conn, player):
    #conn.send(str.encode("Connected"))
    conn.send(str.encode(make_pos(pos[player])))
    reply=""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            #reply = data.decode("utf-8")
            if not data:
                print("Disconnected . . .")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Recieved : ", data)
                print("Sending: ", reply)
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break
    print("lost connection")
    conn.close()

pos  = [(0,0),(100,100)] #starting positions for p1 and p2

currentPlayer = 0

while True:
    conn , addr = s.accept()
    print ("Connected to : ", addr)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
