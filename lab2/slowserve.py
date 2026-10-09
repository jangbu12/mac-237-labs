import http.server
import sys
import time

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(0.3)
        body = b'ok\n'
        self.send_response(200)
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass

class Single(http.server.HTTPServer):
    request_queue_size = 64

class Threaded(http.server.ThreadingHTTPServer):
    request_queue_size = 64

mode = sys.argv[1] if len(sys.argv) > 1 else 'single'
server_class = Threaded if mode == 'threaded' else Single
server = server_class(('127.0.0.1', 8237), Handler)

print(f'{mode} server listening on 127.0.0.1:8237')
server.serve_forever()
