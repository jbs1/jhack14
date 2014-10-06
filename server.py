import socket
import netifaces as ni
import sys
import signal
#from threading import Thread 		# check if still needed
import socketserver


MSG_LEN = 4096
clients = [] 	# client sockets

def updateClients(msg, source):
	global clients
	print("updating all:", msg)
	for client in clients:
		if client is not source:
			client.sendall(msg.encode())

def signal_handler(self, signal, frame):
	print("Shutting down..")
	for client in clients:
		client.close()
	sys.exit(0)

class Server(socketserver.BaseRequestHandler):
	playername = ""

	def receive(self):
		msg = self.request.recv(MSG_LEN).decode()
		print("received:", msg)
		return msg

	def handle(self):
		global clients
		print("connection from", self.client_address)
		clients.append(self.request)
		while True:
			msg = self.receive().strip()
			tokens = msg.split()
			if not tokens:
				clients.remove(self.request)
				updateClients("DISCONNECT " + self.playername, self.request)
				return
			action = tokens.pop(0)
			if action == "CONNECT":
				p = tokens.pop(0)
				if self.playername == "":
					self.playername = p
				print("added player", p)
				updateClients(msg, self.request)
			elif action == "DISCONNECT":
				p = tokens.pop(0)
				if p == playername:
					clients.remove(self.request)
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
host = addrs[ni.AF_INET].pop(0)['addr']
print("Your adress: ", host)

ThreadedTCPServer((host, 9555), Server).serve_forever()
