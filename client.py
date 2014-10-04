from parser import *
from classes import *
from time import sleep
import socket

MSG_LEN = 4096
sock = socket.socket()

print("Textlive - a multiplayer text-adventure")
print("---------------------------------------")

while player.name == "":
	player.name = input("Please enter the name of your Character: ").strip()

host = input("Enter Host Address: ")
sock.connect((host, 9555))
sock.send(("ADD " + player.name).encode())

print("---------------------------------------\n")
print(room.desc)
print("What do you do?")

while True:
    readCmd()
    pOperation()
