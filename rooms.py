from classes import *

sign = Object('sign', 'To the left is a sign.', None, 'The sign says: "Den of Evil"')
opening = Room('You are standing in front of a cave.', {}, {'sign' : sign});
sign.set_room(opening)


opening_w = Room('You are standing in front of an impassable jungle. There is nothing here you can do.')
opening_w.add_room("east", opening)
opening.add_room("west", opening_w)

opening_e = Room('You are standing in front of an impassable jungle. There is nothing here you can do.')
opening_e.add_room("west", opening)
opening.add_room("east", opening_e)


lamp = Item('Lamp', 'An old and rusty oil lamp.', False)
shed = Room('In the dim light from outside you can see a small and dirty room.', {'lamp':lamp}, {}, {}, 'The broken door blocks the entrance')

door=Object('door','The door barely hangs in its place', None, None, 'The door explodes under your force.', None, shed)
opening_s = Room('There is a small shed at west side of the road. A path leads back to the north.', {}, {'door':door})
door.set_room(opening_s)
opening_s.add_room("north", opening)
opening_s.add_room("west", shed)
opening.add_room("south", opening_s)

shed.add_room("east",opening_s)

cave_entrance = Room('You are entering a long tunnel going north, that is dimly lit by the light of your lamp.', {}, {}, {},  'It is to dark to see anything.')
cave_entrance.add_room("south", opening)
opening.add_room("north", cave_entrance)

rooms = {
	'opening' : opening,
	'opening_w' : opening_w,
	'opening_e' : opening_e,
	'opening_s' : opening_s
}
