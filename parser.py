from classes import *
from rooms import *

fillwords = ["the", "with", "on", "that", "at"]
tokens = []
 
def nextToken():
	return tokens.pop(0)

def readCmd():
    global tokens
    line = input('You are standing infront of a cave. To the left is a sign.\n What do you do? \n>> ')
    tokens = line.strip().lower().split()

def pObject(op):
	global fillwords
	obj = nextToken()
	while obj in fillwords:
		obj = nextToken()
	if not obj in room.objects:
		print("You can't ", op, " that.")
		return
	if op == "read":
		room.inspect_obj(obj)

def pItem(op):
	global fillwords
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
			player.drop_item(item) 	# drop

def changeRoom(new_room):
	print(new_room.desc)
	if new_room.traversable:
		room = new_room

def move(direction):
	if direction in ["north", "n"]:
		changeRoom(room.north)
	elif direction in ["east", "e"]:
		changeRoom(room.north)
	elif direction in ["south", "s"]:
		changeRoom(room.south)
	elif direction in ["west", "w"]:
		changeRoom(room.west)

def pDirection():
	direction = nextToken()
	while direction in fillwords:
		direction = nextToken()

	if direction in ["nort", "east", "south", "west", "n", "e", "s", "w"]:
		move(direction)
	else:
		print("I can't go there.")

def attack(target):
	# roll the dice * hitchance
	return None

def pTarget():
	global fillwords
	target = nextToken()
	while target in fillwords:
		target = nextToken()
	if target in entities:
		attack(target)
	else:
		print("I can't attack that.")

def pOperation():
	global fillwords
	op = nextToken()
	while op in fillwords:
		op = nextToken()

	if op == "go":
		pDirection()
	elif op in ["nort", "east", "south", "west", "n", "e", "s", "w"]:
		move(op)
	elif op == "read":
		pObject(op)
	elif op == "take":
		pItem(op)
	elif op == "attack":
		pTarget()
	elif op == "drop":
		pItem(op)
	else:
		print("I dont know that.")

room = rooms['opening']

print("Textlive - a multiplayer text-adventure")
print("---------------------------------------\n")
print(room.desc)

while True:
    readCmd()
    pOperation()
