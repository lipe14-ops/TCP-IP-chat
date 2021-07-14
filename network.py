import socket

class Client:
    def __init__(self, host, port):
        self.addr = (host, port)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.addr)
        print('connection established')
    
    def send_message(self, message):
        try:
            self.client.send(message.encode('utf-8'))
        except Exception:
            print('connection lost.')
            self.client.close()
            exit()
    
    def recv_message(self):
        data = self.client.recv(1028).decode('utf-8')
        if not data:
            print('connection lost.')
            self.client.close()
            exit()
        print(data)