from parser import *
from classes import *
from random import seed,randint
from time import sleep
import netifaces as ni
import socket

ishost = False
 

seed()

print("Textlive - a multiplayer text-adventure")
print("---------------------------------------\n")
player = Player(input("Please enter the name of your Character: ").strip())

s = socket.socket()
c = None
if input("Do you want to host a game? (default: no)\n>> ").strip().lower() in ["yes", "y"]:
	ishost = True
	#print("Your adress: ", socket.gethostbyname(socket.gethostname()))
	#s.bind((socket.gethostbyname(socket.gethostname()), 9555))
	addrs = ni.ifaddresses('wlan0')
	host = addrs[ni.AF_INET].pop(0)['addr']
	print("Your adress: ", host)
	s.bind((host, 9555))

	s.listen(3)

	while True:
		c, addr = s.accept()
		print("connection from ", addr)
else:
	host = input("Enter Host Adress: ")
	print(host)
	s.connect((host, 9555))

print("---------------------------------------\n\n")
print(room.desc)
print("What do you do?")

while True:
    readCmd()
    pOperation()

if ishost:
	s.close()
	c.close()
