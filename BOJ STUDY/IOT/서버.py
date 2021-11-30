import socket

class 웹서버:
    def __init__(self,포트):
        self.포트 = 포트

    def 시작(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        server.bind(("0.0.0.0",self.포트))

        self.server = server
        server.listen()

        while True:
            client, addr = server.accept()
            raw = client.recv(8000)
            data = raw.decode("utf-8")
            if data.startswith("GET /hello HTTP/1.1") == True:
                file = open("hello.html","r")
                html = file.read()
                print(html)
                response = "HTTP/1.1 200 OK\r\nContent-Length: {}\r\n\r\n{}".format(
                    len(html.encode("utf-8")),
                    html
                ).encode("utf-8")
                print(response)
                client.send(response)
                print("오케이")

            else :
                print("잘못되었어")

            client.close()

내서버 = 웹서버(8888)
내서버.시작()