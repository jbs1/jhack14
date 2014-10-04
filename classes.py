"""Class Decleration"""

class player:
	"""player class
	name,health,inf, hitchance"""
	def __init__(self,name):
		self.name=name
		self.health=100
		self.hitchance=0.3
		self.inventory=[]
	def take_item(self,item):
		self.inventory.append(item)
		return "Taking "
	def drop_item(self,item):
		self.inventory.remove(item)
		return "Taking "
	def lose_health(self,dmg):
		self.health=self.health-dmg
		return "You lost "
	def gain_health(self,heal):
		self.health=self.health+heal
		return "You healed "
	def check_health(self):
		if self.health==100:
			print("You are fully healed.")
		elif self.health>=70:
			print("You have minour wounds.")
		elif self.health>=50:
			print("You have bigger wounds.")
		elif self.health>=10:
			print("You have major, life-threatening wounds.")
		elif self.health>=1:
			print("You are as good as dead.")
		elif self.health<=0:
			print("You are DEAD!")


class entity:
	"""docstring for entity"""
	def __init__(self, name, health=100,hitchance=0.3):
		self.name=name
		self.health=health
		self.hitchance=hitchance
	def attack(self,dmg):
		self.health=self.health-dmg
		return "You lost "
	def check_health(self):
		if self.health==100:
			print(self.name,"are fully healed.")
		elif self.health>=70:
			print(self.name,"has minour wounds.")
		elif self.health>=50:
			print(self.name,"has bigger wounds.")
		elif self.health>=10:
			print(self.name,"has major, life-threatening wounds.")
		elif self.health>=1:
			print(self.name,"is nearly dead. Time for the final blow.")
		elif self.health<=0:
			print(self.name,"was killed by you. Good job!")


class room:
	"""docstring for room"""
	def __init__(self, desc, items=[], obj=[]):
		self.desc=desc
		self.items=items
		self.obj=obj
	def add_item(self,item):
		self.items.append(item)
		print("You dropped ")
	def remove_item(self,item):
		self.items.index(item)
		print("You took ")

	def inspect_obj(self,obj):
		print("OBJECT DATA")


class item:
	""" docstring from item"""
	def __init__(self,name):
		self.name=name

class object:
	""" xxx """
	def __init__(self,name,data=None):
		self.name=name
		self.data=data
	def change_data(self,newdata):
		self.data=newdata



		

p=player("jbs")
print(p.health)

print(p.take_item("something"))
print(p.take_item("something else"))
p.gain_health(50)
print(p.health)
