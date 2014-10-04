from parser import *
from classes import *
from time import sleep
import socket
import signal
import sys

def signal_handler(signal, frame):
	print("Shutting down..")
	sock.close()
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

MSG_LEN = 4096
sock = socket.socket()

print("Textlive - a multiplayer text-adventure")
print("---------------------------------------")

while player.name == "":
	player.name = input("Please enter the name of your Character: ").strip()

host = input("Enter Host Address: ")
sock.connect((host, 9555))
sock.send(("CONNECT " + player.name).encode())

print("---------------------------------------\n")
print(room.desc)
print("What do you do?")

while True:
    readCmd()
    pOperation()
