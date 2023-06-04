import http.server
import socketserver
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello world')
        f = open("demofile2.txt", "a")
        f.write("1 \n")
        f.close()


httpd = socketserver.TCPServer(('', 8080), Handler)
httpd.serve_forever()