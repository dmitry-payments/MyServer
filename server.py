import http.server
import socketserver
from http import HTTPStatus
import psycopg2

conn = psycopg2.connect(database="db_name",
                        host="db_host",
                        user="postgres",
                        password="example",
                        port="5432")


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello world')
        f = open("demofile2.txt", "a")
        f.write("1 \n")
        f.close()
        cursor = conn.cursor()
        result = cur.fetchall()
        print(result)



httpd = socketserver.TCPServer(('', 8080), Handler)
httpd.serve_forever()