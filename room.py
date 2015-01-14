class Room:
	"""
	Room Class:
	items/object/entities are dicts with keys the same as the names
	west/east/south/north are room objects
	"""
	def __init__(self, name, desc, items = {}, objects = {}, entities = {}, travers_desc=None, north=None, south=None, west=None, east=None):
		"""
		travers_desc: if not None the room object is blocked and the travers_desc will be printed until room is unblocked by other function
		"""
		self.name = name
		self.desc = desc
		self.items = items
		self.objects = objects
		self.entities = entities
		self.west = west
		self.east = east
		self.north = north
		self.south = south
		self.travers_desc = travers_desc
	
	def open_access(self):
		self.travers_desc = None

	def add_item(self,item):		#add_item(player.drop_item('something'))
		self.items[item.name] = item

	def get_items(self):
		return list(self.items.keys())

	def get_objects(self):
		return list(self.objects.keys())

	def get_entities(self):
		return list(self.entities.keys())
	
	def remove_item(self,item):		# string input 
		tmp = self.items[item]
		del self.items[item]
		return tmp

	def remove_entity(self,entity):		# string input 
		tmp = self.entities[entity]
		del self.entities[entity]
		return tmp

	def inspect_obj(self,obj):		# string input
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