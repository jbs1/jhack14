class Player:
	"""player class"""
	def __init__(self, name):
		self.name = name
		self.health = 100
		self.hitchance = 0.3
		self.inventory = {}
		self.room = None

	def gethitchance(self):
		hc = self.hitchance
		tmp = self.inventory.get('Sword')
		if tmp:
			hc += 0.4
		return hc

	def get_room(self):
		return self.room

	def get_inv(self):
		if self.inventory=={}:
			print("Your inventory is empty. Get more stuff!")
		else:
			print("Your inventory:")
			for i in self.inventory:
				print(self.inventory[i].name)

	def check_inv_item(self,item):
		for i in self.inventory:
			if self.inventory[i].name == item:
				return True

	def take_item(self, item): 			#take_item(room.remove_item('something'))
		self.inventory[item.name] = item
		print("Taking", item.name)

	def drop_item(self, item): 			# string input
		print ("Dropping", item)
		item_b = self.inventory[item]
		del self.inventory[item]
		return item_b

	def attack(self, dmg):
		self.health = self.health - dmg
		if self.health > 0:
			print("You were hurt!")			# write own "checkhealth" for attack() and defend()
		check_health()

	def gain_health(self, heal):
		self.health = self.health + heal
		print("You were healed!")

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
