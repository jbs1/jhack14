class Object:
	""" xxx """
	def __init__(self, name, desc, data = None, break_d=None, open_d=None, blocking=None):
		self.name = name
		self.desc = desc
		self.data = data
		self.blocking = blocking
	def change_data(self, newdata):
		self.data = newdata
	def trigger(self,op):
		if op=="break": 
			if break_d==None:
				print("You can't break this")
			else:
				print(break_d)
				blocking.open_access();

		if op=="open": 
			if open_d==None:
				print("You can't open this")
			else:
				print(open_d)
				blocking.open_access();
