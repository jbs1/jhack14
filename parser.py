from classes import *
from rooms import *
from random import seed,randint
import socket

fillwords = ["the", "with", "on", "that", "at"]
tokens = []
 
def nextToken():
	global tokens
	if not tokens:
		print("I don't know that.")
		return None
	return tokens.pop(0)

def readCmd():
    global tokens
    line = input('>> ')
    tokens = line.strip().lower().split()

def pObject(op):
	obj = nextToken()
	while obj in fillwords:
		obj = nextToken()
	if not obj in room.objects:
		print("You can't ", op, " that.")
		return
	if op == "read":
		room.inspect_obj(obj)

def pItem(op):
	item = nextToken()
	while item in fillwords:
		item = nextToken()

	if item in room.items: 			# room item
		if op == "take":
			player.take_item(room.remove_item(item)) 	# pick up
		elif op == "drop":
			print("I can't drop stuff I didn't pick up.")
	elif item in player.items:		# player inventory item
		if op == "take":
			print("I already have that.")
		elif op == "drop":
			room.add_item(player.drop_item(item)) 	# drop

def changeRoom(new_room):
	global room
	if new_room == None:
		print("You can't go there.")
		return
	if new_room.travers_desc==None:
		print(new_room.desc)
		room = new_room
	else:
		print(new_room.travers_desc)


def move(direction):
	if direction in ["north", "n"]:
		changeRoom(room.north)
	elif direction in ["east", "e"]:
		changeRoom(room.east)
	elif direction in ["south", "s"]:
		changeRoom(room.south)
	elif direction in ["west", "w"]:
		changeRoom(room.west)

def pDirection():
	direction = nextToken()
	while direction in fillwords:
		direction = nextToken()

	if direction in ["north", "east", "south", "west", "n", "e", "s", "w"]:
		move(direction)
	else:
		print("I can't go there.")

def attack(target):
	global player
	if randint(1,10)/10 <= player.gethitc():
		if randint(1,3) == 2:
			print("CRITICAL HIT!")
			target.attack(45)
		else:
			target.attack(20)

def defend(enemy):
	global player
	if randint(1,10)/10 <= enemy.hitchance:
		if randint(1,3) == 2:
			print("CRITICAL HIT!")
			target.attack(35)
		else:
			target.attack(15)

def pTarget():
	target = nextToken()
	while target in fillwords:
		target = nextToken()
	if target in entities:
		attack(target)
	else:
		print("I can't attack that.")

def pAccess(op):
	obj = nextToken()
	while obj in fillwords:
		obj = nextToken()
	obj.trigger(op)

def pOperation():
	op = nextToken()
	while op in fillwords:
		op = nextToken()

	if op == "go":
		pDirection()
	elif op in ["north", "east", "south", "west", "n", "e", "s", "w"]:
		move(op)
	elif op == "look":
		print(room.desc)
	elif op == "read":
		pObject(op)
	elif op == "take":
		pItem(op)
	elif op == "attack":
		pTarget()
	elif op == "drop":
		pItem(op)
	elif op in ["break", "open"]:
		pAccess(op)
	elif op == None:
		pass
	else:
		print("I dont know that.")

seed()
room = rooms['opening']
lord = Entity("The Black Lord")

print("Textlive - a multiplayer text-adventure")
print("---------------------------------------\n")
player = Player(input("Please enter the name of your Character: ").strip())

s = socket.socket()
if input("Do you want to host a game? (default: no)\n>> ").strip().lower() in ["yes", "y"]:
	print("hostname: ", socket.gethostbyname(socket.gethostname()))
	s.bind((socket.gethostbyname(socket.gethostname()), 9555))
	s.listen(3)

	while True:
		c, addr = s.accept()
		print("connection from ", addr)
		c.close()
else:
	host = input("Enter Host Adress: ")
	print(host)
	s.connect((host, 9555))
	s.close()

print("---------------------------------------\n\n")
print(room.desc)
print("What do you do?")

while True:
    readCmd()
    pOperation()
