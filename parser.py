
fillwords = ["the", "with", "on", "that"]
tokens = []
room

def nextToken():
	return tokens.pop(0)

def readCmd():
    global tokens
    line = input('You are standing infront of a cave. To the left is a sign.\n What do you do? \n>> ')
    tokens = line.strip().lower().split()

def object(op):
	global fillwords
	obj = nextToken()
	while obj in fillwords:
		obj = nextToken()
	if not obj in room.objects:
		print("You can't ", op, " that.")

def operation():
	global fillwords
	op = readToken()
	if op == "read":
		# expect object
		object(op)
	elif op == "take":
		# expect item
	elif op == "attack":
		# expect target entity / object
	elif op == "drop":
		# expect item
	elif op in fillwords:
		# ignore fill-words

while True:
    readCmd()
    operation()
