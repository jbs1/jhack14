from classes import *

sign = Object('sign', 'The sign says: "Den of Evil"', '')
opening = Room('You are standing infront of a cave. To the left is a sign.', {}, {'sign' : sign});

opening_w = Room('You are standing infront of an inpassible jungle. There is nothing here you can do.', {}, {})

rooms = {
	'opening' : opening
}
