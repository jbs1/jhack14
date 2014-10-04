import socket
import netifaces as ni

MSG_LEN = 4096
clients = []
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def updateClients(msg, source):
	for client in clients:
		if client is source:
			return
		client.send(msg.encode())

def receive(client):
	return client.recv(MSG_LEN).decode()

def handleConnection(client):
	while True:
		msg = receive(client)

		print("received player name: ", name)
	client.close()
	
addrs = ni.ifaddresses('wlan0')
host = addrs[ni.AF_INET].pop(0)['addr']
print("Your adress: ", host)
sock.bind((host, 9555))

sock.listen(3)
while True:
	client, addr = sock.accept()
	print("connection from ", addr)
	clients.append(client)
	handleConnection(client)
