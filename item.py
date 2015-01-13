class Item:
	"""
	Item class:
	Items are objects that can be picked up/interacted with and put into the inventory.
	Exp: lamp item
	"""
	def __init__(self, name, desc, data=None):
		self.name = name
		self.desc = desc
		self.data = data
		
	def change_data(self, newdata):
		self.data = newdata
	