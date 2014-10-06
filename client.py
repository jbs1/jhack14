from parser import *
from classes import *
from time import sleep
import signal
import threading
from sys import exit

def signal_handler(signal, frame):
	print("Shutting down..")
	send("DISCONNECT " + player.name)
	sleep(1)		# shutdown grace time
	sock.close()
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

MSG_LEN = 4096
players = {}

def receive():
	return sock.recv(MSG_LEN).decode()

def receiveFromServer():
	global players
	while True:
		msg = receive().strip().split()
		print("received: ", msg)
		if not msg:
			print("Disconnected from server. Shutting down..")
			sock.close()
			exit(2)
		token = msg.pop(0)
		if token == "CONNECT":
			p = msg.pop(0)
			players[p] = Player(p)
			print("added player", p)
		elif token == "DISCONNECT":
			p = msg.pop(0)
			del players[p]
			print("removed player", p)
		elif token == "MOVE":
			p = msg.pop(0)
			d = msg.pop(0)
			move(p, d)
		elif token == "SET":
			obj = msg.pop(0)
			msg.pop(0) 			# skip 'IN'
			room = msg.pop(0)
			msg.pop(0) 			# skip 'TO'
			status = msg.pop(0)	
			if status == "OPEN":
				rooms[room].objects[obj].trigger("open")
			elif status == "BREAK":
				rooms[room].objects[obj].trigger("break")
		elif token == "DECREASE":
			msg.pop(0)			# skip 'HEALTH'
			msg.pop(0)			# skip 'OF'
			p = msg.pop(0)
			msg.pop(0) 			# skip 'BY'
			amount = msg.pop(0)	
			if p.lower() in ["wizard", "dark lord", "goblin"]:
				lord.attack(amount)
			else:
				players[p].lose_health(amount)
		elif token == "COPY":
			item = msg.pop(0)
			msg.pop(0) 			# skip 'FROM'
			p = msg.pop(0)
			player.take_item(players[p].inventory[item])
		else:
			print("Unkown action in receiveFromServer()")
			break

print("Textlive - a multiplayer text-adventure")
print("---------------------------------------")

while player.name == "":
	player.name = input("Please enter the name of your Character: ").strip()
host = input("Enter Host Address: ")
if host == "":
	host = "10.81.63.17"
sock.connect((host, 9555))
send("CONNECT " + player.name)

threading.Thread(target=receiveFromServer, daemon=True).start()

print("---------------------------------------\n")
print(player.room.desc)
print("What do you do?")

while True:
    readCmd()
    pOperation()
