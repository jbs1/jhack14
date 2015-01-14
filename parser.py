from classes import *
from random import seed, randint
import socket
from time import sleep
from sys import exit

fillwords = ["the", "with", "on", "that", "at", "go", "to"]
tokens = []

seed()
player = Player("") #player variable is allways the local player
player.room = rooms['opening']
#boss = Entity("The Black Lord")   not used
sock = socket.socket()

def send(msg):
	sock.send(msg.encode())
	print("send:", msg)

#p. < is the player adressed by the server
def changeRoom(p, new_room):
	if new_room == None:
		print("You can't go there.")
		return
	if new_room == cave_entrance:
		checked = False #checked is necesary to prevent muliple open_access on cave_entrance
		if lamp.data == True and checked == False:
			cave_entrance.open_access()
			checked = True
	if new_room.travers_desc == None: #if travers_desc is not None the new room is blocked and
		print(new_room.desc)	#the travers_desc is printed to explain how its blocked
		p.room = new_room
		for i in p.room.items:
			print(p.room.items[i].desc)
		for i in p.room.objects:
			print(p.room.objects[i].desc)
		for i in p.room.entities:
			print(p.room.entities[i].desc)
	else:
		print(new_room.travers_desc)

def move(p, direction):

	while direction in fillwords:
		direction = nextToken()

	if direction in ["north", "east", "south", "west", "n", "e", "s", "w"]:
		if direction in ["north", "n"]:
			changeRoom(p, p.room.north)
		elif direction in ["east", "e"]:
			changeRoom(p, p.room.east)
		elif direction in ["south", "s"]:
			changeRoom(p, p.room.south)
		elif direction in ["west", "w"]:
			changeRoom(p, p.room.west)
	else:
		print("I can't go there.")


def attack(target):
	"""
	player attacks target
	"""
	global player
	if randint(1,10) / 10 <= player.gethitchance():
		if randint(1,3) == 2:
			target.lose_health(45,True)
			defend(target)
		else:
			target.lose_health(20)
			defend(target)
	else:
		print("You missed!")
		target.check_health()
		defend(target)

def defend(enemy):
	"""
	player gets attacked by target
	"""
	global player
	if randint(1,10) / 10 <= enemy.gethitchance():
		if randint(1,3) == 2:
			player.lose_health(35,True)
		else:
			player.lose_health(15)
	else:
		print(enemy.name, "missed!")
		player.check_health()

def nextToken():
	"""goes throught list of input tokes"""
	global tokens
	if not tokens:
		print("I don't know that.")
		return None
	print("DEBUG:",tokens[0])	#DEBUG USE
	return tokens.pop(0)

def readCmd():
	"""makes input to list of tokens"""
	global tokens
	line = input('>> ')
	tokens = line.strip().lower().split()

def pObject(op):
	obj = nextToken()
	while obj in fillwords:
		obj = nextToken()
	if not obj in player.room.objects:
		print("You can't ", op, " that.")
		return
	if op == "read":
		player.room.inspect_obj(obj)

def pItem(op):
	global player
	item = nextToken()
	while item in fillwords:
		item = nextToken()

	if item in player.room.get_items(): 			# room item
		if op == "take":
			player.take_item(player.room.remove_item(item)) 	# pick up
		elif op == "drop":
			print("I can't drop stuff I didn't pick up.")
	elif item in player.get_inv_list():			# player inventory item
		if op == "take":
			print("I already have that.")
		elif op == "drop":
			player.room.add_item(player.drop_item(item)) 		# drop
	else:
		print("What item?")

# def pDirection():
# 	while direction in fillwords:
# 		direction = nextToken()

# 	if direction in ["north", "east", "south", "west", "n", "e", "s", "w"]:
# 		move(player, direction)
# 	else:
# 		print("I can't go there.")

def pTarget():
	target = nextToken()	
	while target in fillwords:
		target = nextToken()
	if target in player.room.get_entities():
		attack(player.room.entities[target])
	else:
		print("I can't attack that.")

def pAccess(op):
	obj = nextToken()
	while obj in fillwords:
		obj = nextToken()
	if obj in player.room.get_objects():
		player.room.objects[obj].trigger(op)
		send("SET " + obj + " IN " + player.room.name + " TO " + op.upper())
	else:
		print("Can't", op, "that.")

def pOperation():
	op = nextToken()
	while op in fillwords:
		op = nextToken()

	#if op == "go": ==>go added to fill words
	#	pDirection()
	if op in ["north", "east", "south", "west", "n", "e", "s", "w"]:
		move(player, op)
	elif op in ["look", "l"]:
		print(player.room.desc)
		for i in player.room.items:
			print(player.room.items[i].desc)
		for i in player.room.objects:
			print(player.room.objects[i].desc)
		for i in player.room.entities:
			print(player.room.entities[i].desc)
	elif op == "read":
		pObject(op)
	elif op == "take":
		pItem(op)
	elif op == "attack":
		pTarget()
	elif op == "drop":
		pItem(op)
	elif op in ["i", "inventory", "inv"]:
		player.get_inv()
	elif op in ["turnon", "light"]:
		lamp.change_data(True)
		lamp.update_name("Lamp[ON]")
	elif op in ["break", "open"]:
		pAccess(op)
	elif op == "hc":		# debug only
		print("HC:", player.gethitchance())
	elif op == "exit":
		send("DISCONNECT " + player.name)
		sleep(2)
		exit()
	elif op == None:
		pass
	elif op == "debug":
		print("*******************************\nDEBUG MENU:\n\n[1] open access to cave\n*******************************")
		dinp=input("DEBUGinput:")
		if dinp == '1':
			cave_entrance.open_access()
			print("OPENED \n\n\n\n")


	else:
		print("I dont know that.")

