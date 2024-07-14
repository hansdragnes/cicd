from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'lokal senere commit paa hans branch')

port = int(os.environ.get('PORT', 3000))

httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
print(f'Server running on port {port}')
httpd.serve_forever()