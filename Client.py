import threading
lock = threading.Lock()

class Client:
    def __init__(self):
        self.users = {}

    def add(self, username, conn, addr):
        if username in self.users:
            conn.send('이미 존재하는 닉네임입니다.\n'.eocode())
            return None
        
        lock.acquire()
        self.users[username] = (conn, addr)
        lock.release()

        self.sendMessageToAll(username + '님이 입장하셨습니다.')
        print('- 현재 대화 인원: ' + str(len(self.users)))

        return username

    def remove(self, username):
        if username not in self.users:
            return
        
        lock.acquire()
        del self.users[username]
        lock.release()

        self.sendMessageToAll(username + '님이 퇴장하셨습니다.')
        print('- 현재 대화 인원: ' + str(len(self.users)))

    def receive(self, username, msg, db):
        print(username + "님이 " + msg + "를 입력했습니다.\n")
        if msg[0] != '!':
            self.sendMessageToAll('[' + username + '] ' + msg)
            return
        msg = msg.strip()
        if msg == '!q':
            self.remove(username)
            return -1

    def sendMessageToAll(self, msg):
        for conn,_ in self.users.values():
            conn.send(msg.encode())