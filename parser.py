from classes import *
from random import seed, randint
import socket

fillwords = ["the", "with", "on", "that", "at"]
tokens = []

seed()
player = Player("")
player.room = rooms['opening']
lord = Entity("The Black Lord")
sock = socket.socket()

def send(msg):
	sock.send(msg.encode())
	print("send: ", msg)

def changeRoom(p, new_room):
	if new_room == None:
		print("You can't go there.")
		return
	if new_room == cave_entrance:
		checked=False
		if lamp.data==True and checked==False:
			cave_entrance.open_access()
			checked=True
	if new_room.travers_desc == None:
		print(new_room.desc)
		p.room = new_room
		for i in p.room.items:
			print(p.room.items[i].desc)
		for i in p.room.objects:
			print(p.room.objects[i].desc)
		for i in p.room.entities:
			print(p.room.entities[i].name)
	else:
		print(new_room.travers_desc)

def move(p, direction):
	if direction in ["north", "n"]:
		changeRoom(p, p.room.north)
	elif direction in ["east", "e"]:
		changeRoom(p, p.room.east)
	elif direction in ["south", "s"]:
		changeRoom(p, p.room.south)
	elif direction in ["west", "w"]:
		changeRoom(p, p.room.west)

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
	if item in player.room.items.keys(): 			# room item
		if op == "take":
			player.take_item(player.room.remove_item(item)) 	# pick up
	else:
		print("What item?")
		#elif op == "drop":
			#print("I can't drop stuff I didn't pick up.")
	"""elif item in player.inventory.keys():		# player inventory item
		if op == "take":
			print("I already have that.")
		elif op == "drop":
			player.room.add_item(player.drop_item(item)) 	# drop"""

		
def pDirection():
	direction = nextToken()
	while direction in fillwords:
		direction = nextToken()

	if direction in ["north", "east", "south", "west", "n", "e", "s", "w"]:
		move(player, direction)
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
	if obj in player.room.objects.keys():
		player.room.objects[obj].trigger(op)
		send("SET " + obj + " IN " + player.room.name + " TO " + op.upper())
	else:
		print("Can't ", op, "that.")

	

def pOperation():
	op = nextToken()
	while op in fillwords:
		op = nextToken()

	if op == "go":
		pDirection()
	elif op in ["north", "east", "south", "west", "n", "e", "s", "w"]:
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
	#elif op == "drop":
	#	pItem(op)
	elif op in ["i", "inventory", "inv"]:
		player.get_inv()
	elif op in ["turnon", "light"]:
		lamp.change_data(True)
	elif op in ["break", "open"]:
		pAccess(op)
	elif op == "hc":
		print("HC:",player.gethitc())
	elif op == None:
		pass
	else:
		print("I dont know that.")
