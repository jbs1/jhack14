class Object:
	"""Object Class"""
	def __init__(self, name, desc, room, data=None, break_d=None, open_d=None, blocking=None):
		self.name = name
		self.desc = desc
		self.room = room
		self.data = data
		self.break_d = break_d
		self.open_d = open_d
		self.blocking = blocking

	def change_data(self, newdata):
		self.data = newdata

	def set_room(self, room):
		self.room = room

	def trigger(self, op):		# move method to room class!!
		if op == "break": 
			if self.break_d == None:
				print("You can't break this")
			else:
				print(self.break_d)
				self.blocking.open_access();
				del self.room.objects[self.name];
		elif op == "open": 
			if self.open_d == None:
				print("You can't open this")
			else:
				print(self.open_d)
				self.blocking.open_access();
