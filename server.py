import socket
import netifaces as ni
import sys
import signal
import threading
import socketserver
from player import *


MSG_LEN = 4096
clients = []	# client sockets
players = {}    # player data

"""
    Updates all the clients connected to the server,
    except for the client who is the source of the msg
    (if one is specified).
"""
def updateClients(msg, source=None):
	global clients
	for client in clients:
		if client is not source:
			print("updating", str(client))
			client.sendall(msg.encode())
"""
    Updates a single client with a message.
"""
def updateClient(msg, client):
    print("updating", str(client))
    client.sendall(msg.encode())

"""
    Catches SIGINT's to provide for a cleaner shutdown.
"""
def signal_handler(self, signal, frame=None):
	global clients
	global tserver
	print("Shutting down..")
	for client in clients:
		client.close()
	# TODO shutdown / close threadedTcpServer!
	tserver.shutdown()
	tserver.socket.close()

class Server(socketserver.BaseRequestHandler):
	playername = ""

	def receive(self):
		msg = self.request.recv(MSG_LEN).decode()
		print("received:", msg)
		return msg

	def handle(self):
		global clients
		global players
		print("connection from", self.client_address)
		clients.append(self.request)
		while True:
			msg = self.receive().strip()
			tokens = msg.split()
			if not tokens:
				clients.remove(self.request)				# and this as well (s.b.)
				del players[self.playername]			# check if this works
				updateClients("DISCONNECT " + self.playername, self.request)
				break
			action = tokens.pop(0)
			if action == "CONNECT":
				p = tokens.pop(0)
				if self.playername == "":       # initial connection
					for name in players.keys():	# send player list
						updateClient("CONNECT " + name, self.request)
					self.playername = p			# create own player obj
					players[p] = Player(p)
				print("added player", p)
				updateClients(msg, self.request)
			elif action == "DISCONNECT":
				p = tokens.pop(0)
				if p == self.playername:
					break
					#clients.remove(self.request)
				print("removing player", p)
				updateClients(msg, self.request)
			elif action in ["MOVE", "SET", "DECREASE", "COPY"]:
				updateClients(msg, self.request)
			else:
				print("Unkown action in handleConnection()")
				break
		self.request.close()


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
	pass

signal.signal(signal.SIGINT, signal_handler)

addrs = ni.ifaddresses('wlan0')
if ni.AF_INET in addrs.keys():
    host = addrs[ni.AF_INET].pop(0)['addr']
else:
    host = "127.0.0.1"
print("Your address: ", host)

# create new threaded server ..
ThreadedTCPServer.allow_reuse_address = True
tserver = ThreadedTCPServer((host, 9555), Server)

# .. and run it in its own thread
server_thread = threading.Thread(target=tserver.serve_forever)
server_thread.start()

