import socketserver
from Client import Client
from db import DB

db = DB()
class MyTcpHandler(socketserver.BaseRequestHandler):
    user = Client()

    def handle(self):
        try:
            username = self.register()
            msg = self.request.recv(1024)
            while msg:
                if self.user.receive(username, msg.decode(), db) == -1:
                    self.request.close()
                    break
                msg = self.request.recv(1024)
        except Exception as e:
            print(e)

    def register(self):
        while True:
            self.request.send('로그인 ID:'.encode())
            username = self.request.recv(1024)
            username = username.decode().strip()
            if self.user.add(username, self.request, self.client_address):
                return username

class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass