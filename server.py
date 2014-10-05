import socket
import netifaces as ni
import sys
import signal
from classes import *
from threading import Thread
import socketserver


MSG_LEN = 4096
clients = [] 	# client sockets
players = {}

def updateClients(msg, source):
	global clients
	for client in clients:
		if client is source:
			return
		client.sendall(msg.encode())
		print("sending to all: ", msg)


class Server(socketserver.BaseRequestHandler):
	playername = None
	"""
	def signal_handler(self, signal, frame):
		print("Shutting down..")
		for client in clients:
			client.close()
	#	sock.close()
		sys.exit(0)
	"""

	def receive(self):
		msg = self.request.recv(MSG_LEN).decode()
		print("received: ", msg)
		return msg

	def handle(self):
		global players
		print("connection from ", self.client_address)
		clients.append(self.request)
		while True:
			msg_bak = self.receive().strip()
			msg = msg_bak.split()
			if not msg:
				clients.remove(self.request)
				updateClients("DISCONNECT " + self.playername, self.request)
				del players[p]
				return
			first = msg.pop(0)
			if first == "CONNECT":
				p = msg.pop(0)
				players[p] = Player(p)
				print("added player", p)
				if self.playername == None:
					self.playername = p
				updateClients(msg_bak, self.request)
			elif first == "DISCONNECT":
				p = msg.pop(0)
				if players[p]:
					del players[p]
					print("removed player", p)
				updateClients(msg_bak, self.request)
			elif first == "MOVE":
				p = msg.pop(0)
				d = msg.pop(0)
				updateClients(msg_bak, self.request)
			elif first == "SET":
				obj = msg.pop(0	)
				msg.pop(0) 			# skip 'IN'
				room = msg.pop(0)
				msg.pop(0) 			# skip 'TO'
				status = msg.pop(0)	
				if status in ["OPEN", "BREAK"]:
					updateClients(msg_bak, self.request)
			elif first == "DECREASE":
				msg.pop(0)			# skip 'HEALTH'
				msg.pop(0)			# skip 'OF'
				p = msg.pop(0)
				msg.pop(0) 			# skip 'BY'
				amount = msg.pop(0)	
				updateClients(msg_bak, self.request)
			elif first == "COPY":
				item = msg.pop(0)
				msg.pop(0) 			# skip 'FROM'
				player = msg.pop(0)
				updateClients(msg_bak, self.request)
			else:
				print("Unkown action in handleConnection()")
				break
		self.request.close()


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
	pass

	
addrs = ni.ifaddresses('wlan0')
host = addrs[ni.AF_INET].pop(0)['addr']
print("Your adress: ", host)
#sock.bind((host, 9555))

#sock.listen(10)
ThreadedTCPServer((host, 9555), Server).serve_forever()

"""
while True:
	client, addr = sock.accept()
	print("connection from ", addr)
	clients.append(client)
	threading.Thread(target=handleConnection(client)).start()

sock.close()
"""