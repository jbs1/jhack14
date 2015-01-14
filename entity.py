import parser #for accessing local player data ==> from parser import player does not work
class Entity:
	"""
	NPC the player can interact with
	"""
	def __init__(self, name, desc, health=100, hitchance=0.5):
		"""
		hitchance is the probabblitiy the entity is going to hit
		"""
		self.name = name
		self.desc = desc
		self.health = health
		self.hitchance = hitchance

	def gethitchance(self):
		return self.hitchance

	def lose_health(self, dmg, ch=False):
		self.health = self.health - dmg
		if ch==True:
			print("CRITICAL HIT:",self.name,"was hurt badly!")
		else:
			print(self.name,"was hurt!")
		self.check_health();

	def gain_health(self, heal):
		self.health = self.health + heal
		print(self.name,"was healed!")
	
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
			tmp_room = parser.player.get_room()
			tmp_room.remove_entity(self.name)
