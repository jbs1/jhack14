class Entity:
	"""docstring for entity"""
	def __init__(self, name, health = 100,hitchance = 0.3):
		self.name = name
		self.health = health
		self.hitchance = hitchance
	def attack(self,dmg):
		self.health = self.health-dmg
		print(self.name,"was hit!")
		check_health();
	def check_health(self):
		if self.health == 100:
			print(self.name,"is fully healed.")
		elif self.health >= 70:
			print(self.name,"has minour wounds.")
		elif self.health >= 50:
			print(self.name,"has bigger wounds.")
		elif self.health >= 10:
			print(self.name,"has major, life-threatening wounds.")
		elif self.health >= 1:
			print(self.name,"is nearly dead. Time for the final blow.")
		elif self.health <= 0:
			print(self.name,"was killed by you. Good job!")
