import socket
import netifaces as ni
import sys
import signal
from classes import *

MSG_LEN = 4096
clients = [] 	# client sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
players = {}

def signal_handler(signal, frame):
	print("Shutting down..")
	for client in clients:
		client.close()
	sock.close()
	sys.exit(0)

def updateClients(msg, source):
	for client in clients:
		if client is source:
			return
		client.send(msg.encode())

def receive(client):
	return client.recv(MSG_LEN).decode()

def handleConnection(client):
	while True:
		msg_bak = receive(client).strip()
		msg = msg_bak.split()
		if not msg:
			return
		first = msg.pop(0)
		if first == "CONNECT":
			p = msg.pop(0)
			players[p] = Player(p)
			print("added player '", p, "'")
			updateClients(msg_bak, client)
		elif first == "DISCONNECT":
			p = msg.pop(0)
			del players[p]
			print("removed player '", p, "'")
			updateClients(msg_bak, client)
		elif first == "MOVE":
			p = msg.pop(0)
			d = msg.pop(0)
			updateClients(msg_bak, client)
		elif first == "SET":
			obj = msg.pop(0)
			msg.pop(0) 			# skip 'IN'
			room = msg.pop(0)
			msg.pop(0) 			# skip 'TO'
			status = msg.pop(0)	
			if status in ["OPEN", "BREAK"]:
				updateClients(msg_bak, client)
		elif first == "DECREASE":
			msg.pop(0)			# skip 'HEALTH'
			msg.pop(0)			# skip 'OF'
			p = msg.pop(0)
			msg.pop(0) 			# skip 'BY'
			amount = msg.pop(0)	
			updateClients(msg_bak, client)
		elif first == "COPY":
			item = msg.pop(0)
			msg.pop(0) 			# skip 'FROM'
			player = msg.pop(0)
			updateClients(msg_bak, client)
		else:
			print("Unkown action in handleConnection()")
			break
	client.close()

signal.signal(signal.SIGINT, signal_handler)
	
addrs = ni.ifaddresses('wlan0')
host = addrs[ni.AF_INET].pop(0)['addr']
print("Your adress: ", host)
sock.bind((host, 9555))

sock.listen(10)
while True:
	client, addr = sock.accept()
	print("connection from ", addr)
	clients.append(client)
	handleConnection(client)

sock.close()
