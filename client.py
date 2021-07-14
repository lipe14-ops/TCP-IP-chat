from network import Client
from threading import Thread

nome = input('nickname: ')

class Chat:
    def __init__(self):
        self.client = Client('127.0.0.1', 12000)

    def receive(self):
        while True:
            try:
                self.client.recv_message()
            except Exception: break

    def run_chat(self):
        while True:
            message = input()
            if message == '':
                continue
            self.client.send_message(f'\033[1;96m{nome}\033[0;0m: {message}')
        
if __name__ == '__main__':
    chat = Chat()
    try:
        Thread(target=chat.receive).start()
        chat.run_chat()
    except Exception:
        print('connection lost.')
        exit()