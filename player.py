class Player:
	"""player class
	name,health,inf, hitchance"""
	def __init__(self,name):
		self.name = name
		self.health = 100
		self.hitchance = 0.3
		self.inventory = {}
	def gethitc(self):
		hc = self.hitchance
		if inventory['Sword']:
			hc += 0.4
		return hc
	def take_item(self,item):#take_item(room.remove_item('something'))
		inventory[item.name] = item
		print("Taking",item.name)
	def drop_item(self,item):#item=string
		print ("Dropping ",item)
		tmp = inventory[item]
		del inventory[item]
		return tmp
	def lose_health(self,dmg):
		self.health = self.health-dmg
		print("You were hurt!")
		check_health()

	"""	def gain_health(self,heal):
		self.health = self.health+heal
		print("You were healed!")"""

	def check_health(self):
		if self.health == 100:
			print("You are fully healed.")
		elif self.health >= 70:
			print("You have minour wounds.")
		elif self.health >= 50:
			print("You have bigger wounds.")
		elif self.health >= 10:
			print("You have major, life-threatening wounds.")
		elif self.health >= 1:
			print("You are as good as dead.")
		elif self.health <= 0:
			print("You are DEAD!")
