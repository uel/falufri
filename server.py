import SimpleHTTPServer
import SocketServer
import socket

PORT = 80

def onRequest(JsonData):
        pass

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def do_POST(self):
                content_len = int(self.headers.getheader('content-length', 0))
                post_body = self.rfile.read(content_len)
                onRequest(post_body)


class MyTCPServer(SocketServer.TCPServer):
        def server_bind(self):
                self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.socket.bind(self.server_address)


Handler = ServerHandler
httpd = MyTCPServer(("", PORT), Handler)
print("[Server] hosting")
httpd.serve_forever()
