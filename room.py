class Room:
	"""docstring for room"""
	def __init__(self, desc, items = {}, objects = {}, north=None, south=None, west=None, east=None):
		self.desc = desc
		self.items = items
		self.objects = objects
		self.west = west
		self.east = east
		self.north = north
		self.south = south
	def add_item(self,item):#add_item(player.drop_item('something'))
		items[item.name]=item
		print("You dropped",item.name)
	def remove_item(self,item):#item=str
		print("You took",item)
		tmp = items[item]
		del items[item]
		return tmp
	def inspect_obj(self,obj):#obj=string
		print(objects[obj].data)