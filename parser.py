from classes import *
from random import seed, randint

fillwords = ["the", "with", "on", "that", "at"]
tokens = []

seed()
room = rooms['opening']
lord = Entity("The Black Lord")


def changeRoom(new_room):
	global room
	if new_room == None:
		print("You can't go there.")
		return
	if new_room.travers_desc==None:
		print(new_room.desc)
		room = new_room
		for i in room.items:
			print(room.items[i].desc)
		for i in room.objects:
			print(room.objects[i].desc)
		for i in room.entities:
			print(room.entities[i].desc)
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
	global player
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

def pDirection():
	direction = nextToken()
	while direction in fillwords:
		direction = nextToken()

	if direction in ["north", "east", "south", "west", "n", "e", "s", "w"]:
		move(direction)
	else:
		print("I can't go there.")

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
	if obj in room.objects.keys():
		room.objects[obj].trigger(op)
	else:
		print("Can't ", op, "that.")
	

def pOperation():
	op = nextToken()
	while op in fillwords:
		op = nextToken()

	if op == "go":
		pDirection()
	elif op in ["north", "east", "south", "west", "n", "e", "s", "w"]:
		move(op)
	elif op in ["look", "l"]:
		print(room.desc)
		for i in room.items:
			print(room.items[i].desc)
		for i in room.objects:
			print(room.objects[i].desc)
		for i in room.entities:
			print(room.entities[i].desc)
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
