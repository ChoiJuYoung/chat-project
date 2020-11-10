from MyTCPHandler import MyTcpHandler
from MyTCPHandler import Server

if __name__ == '__main__':
    try:
        HOST = ''
        PORT = 6600
        server = Server((HOST, PORT), MyTcpHandler)
        server.serve_forever()
        print('server on')
    except KeyboardInterrupt:
        print("SERVER 종료")
        server.shutdown()
        server.server_close()
