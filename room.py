class Room:
	"""docstring for room"""
	def __init__(self, desc, items = {}, objects = {}, entities = {}, travers_desc=None, north=None, south=None, west=None, east=None):
		self.desc = desc
		self.items = items
		self.objects = objects
		self.entities = entities
		self.west = west
		self.east = east
		self.north = north
		self.south = south
		self.travers_desc = travers_desc
	
	def add_item(self,item):		#add_item(player.drop_item('something'))
		self.items[item.name]=item
		print("You dropped",item.name)
	
	def open_access(self):
		self.travers_desc=None


	def remove_item(self,item):		#item=str
		print("You took",item)
		tmp = self.items[item]
		del self.items[item]
		return tmp

	def inspect_obj(self,obj):		#obj=string
		print(self.objects[obj].data)

	def add_room(self, direction, room, travers_desc=None):
		if direction == "north":
			self.north = room
		elif direction == "east":
			self.east = room
		elif direction == "south":
			self.south = room
		elif direction == "west":
			self.west = room