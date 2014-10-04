from parser import *
from classes import *
from time import sleep
import socket

MSG_LEN = 1024

sock = socket.socket()

print("Textlive - a multiplayer text-adventure")
print("---------------------------------------\n")

player = Player(input("Please enter the name of your Character: ").strip())
while player.name == "":
	player.name = input("Please enter the name of your Character: ").strip()

host = input("Enter Host Address: ")
sock.connect((host, 9555))
sock.send(player.name.encode())

print("---------------------------------------\n\n")
print(room.desc)
print("What do you do?")

while True:
    readCmd()
    pOperation()
