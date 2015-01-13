from player import *
import parser #for accessing local player data ==> from parser import player does not work
class Object:
	"""
	Object Class:
	Interacable object within the world.
	Exp:
	a door
	"""

	def __init__(self, name, desc, data=None, break_desc=None, open_desc=None, blocking=None):
		"""
		data is the content if any of 
		break_desc/open_desc: if set obj is breakable/openable, also provied desc of the breaking/opening of obj
		blocking shows the room this onject blocks
		"""
		self.name = name
		self.desc = desc
		#self.room = room <== not needed because its always the player room
		self.data = data
		self.break_desc = break_desc
		self.open_desc = open_desc
		self.blocking = blocking

	def change_data(self, newdata):
		self.data = newdata

	# def set_room(self, room):<==same as above
	# 	self.room = room

	def trigger(self, op):		# move method to room class!!
		"""
		is called as member function of the object it triggers
		"""
		if op == "break": 
			if self.break_desc == None:
				print("You can't break this")
			else:
				print(self.break_desc)
				self.blocking.open_access()
				tmp_room = parser.player.get_room()
				del tmp_room.objects[self.name]#deletes itself here? maybe move > see above
		elif op == "open": 
			if self.open_desc == None:
				print("You can't open this")
			else:
				print(self.open_desc)
				self.blocking.open_access()
