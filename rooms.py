from classes import *

sign = Object('sign', 'The sign says: "Den of Evil"', '')
opening = Room('You are standing infront of a cave. To the left is a sign.', {}, {'sign' : sign});

opening_w = Room('You are standing infront of an inpassible jungle. There is nothing here you can do.', {}, {})
opening_w.add_room("east", opening)
opening.add_room("west", opening_w)

opening_e = Room('You are standing infront of an inpassible jungle. There is nothing here you can do.', {}, {})
opening_e.add_room("west", opening)
opening.add_room("east", opening_e)

rooms = {
	'opening' : opening,
	'opening_w' : opening_w,
	'opening_e' : opening_e
}
