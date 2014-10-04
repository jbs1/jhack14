from classes import *

sign = Object('sign', 'The sign says: "Den of Evil"', '')
opening = Room('You are standing infront of a cave. To the left is a sign.', {}, {'sign' : sign});

opening_w = Room('You are standing infront of an inpassable jungle. There is nothing here you can do.', {}, {})
opening_w.add_room("east", opening)
opening.add_room("west", opening_w)

opening_e = Room('You are standing infront of an inpassable jungle. There is nothing here you can do.', {}, {})
opening_e.add_room("west", opening)
opening.add_room("east", opening_e)


lamp = Object('Lamp', 'An old and rusty oil lamp.', False)
shed = Room('In the dim light from outside you can see a small and dirty room.', {'lamp':lamp}, {}, 'The broken door blocks the entrace')

door=Object('door','The door is barely hangs in its place', None, 'You door explodes under your force', None, shed)
opening_s = Room('There is a small shed at west side of the road.', {}, {'door':door})
opening_s.add_room("north", opening)
opening_s.add_room("west", shed)
opening.add_room("south", opening_s)

shed.add_room("east",opening_s)

cave_entrance = Room("It's to dark to see anything.")
cave_entrance.add_room("south", opening)
opening.add_room("north", cave_entrance)

rooms = {
	'opening' : opening,
	'opening_w' : opening_w,
	'opening_e' : opening_e,
	'opening_s' : opening_s
}
