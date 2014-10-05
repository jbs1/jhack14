class Item:
	""" docstring from item"""
	def __init__(self, name, desc, data=None):
		self.name = name
		self.desc = desc
		self.data = data
	def change_data(self, newdata):
		self.data = newdata
	