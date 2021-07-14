import socket
from threading import Thread

class Server:
	def __init__(self):
		self.connections = []
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.bind(('127.0.0.1', 12000))
		self.server.listen(5)
			
	def handler_client(self, connection, address):
		while True:
			try:
				data  = connection.recv(2028).decode('utf-8')
				for conn in self.connections:
					if conn != connection:
						conn.send(data.encode('utf-8'))
			except Exception:
				for conn in self.connections:
					if conn != connection:
						conn.send(f'\033[1;33m{address} \033[1;91mdisconnect.\033[0;0m'.encode('utf-8'))
				self.connections.remove(connection)
				print(f'\033[1;91mdisconnected with:\033[1;33m {address}\033[0;0m')
				connection.close()
				break

	def receive_player(self):
		connection, address = self.server.accept()
		self.connections.append(connection)
		print(f'connected with: {address}')
		for conn in self.connections:
			if conn != connection:
				conn.send(f'\033[1;33m{address} \033[1;32mconnect.\033[0;0m'.encode('utf-8'))
			else:
				conn.send(f'\033[1;32myou joined in the chat.\033[0;0m'.encode('utf-8'))
		Thread(target=self.handler_client, args=(connection, address)).start()

if __name__ == '__main__':
	server = Server()
	while True:
		try:
			server.receive_player()
		except Exception: pass