"""Small local web interface for FIBB.py. Run: python app.py"""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import os
from urllib.parse import urlsplit

from FIBB import fibonacci_iterative, fibonacci_recursive_series

ROOT = Path(__file__).resolve().parent

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if urlsplit(self.path).path != '/':
            self.send_error(404)
            return
        content = (ROOT / 'index.html').read_bytes()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_POST(self):
        if urlsplit(self.path).path != '/api/generate':
            self.send_error(404)
            return
        try:
            size = int(self.headers.get('Content-Length', '0'))
            if size < 1 or size > 1024:
                raise ValueError('Invalid request size.')
            data = json.loads(self.rfile.read(size))
            n = data.get('terms')
            method = data.get('method')
            if type(n) is not int or not 1 <= n <= 100:
                raise ValueError('Enter a whole number from 1 to 100.')
            if method not in ('iterative', 'recursive'):
                raise ValueError('Choose an available method.')
            if method == 'recursive' and n > 30:
                raise ValueError('Recursive mode supports up to 30 terms.')
            series = fibonacci_iterative(n) if method == 'iterative' else fibonacci_recursive_series(n)
            self.respond(200, {'series': series, 'terms': n, 'method': method})
        except (ValueError, TypeError, json.JSONDecodeError) as exc:
            self.respond(400, {'error': str(exc)})

    def respond(self, status, obj):
        payload = json.dumps(obj).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    server = ThreadingHTTPServer(('0.0.0.0', port), Handler)
    print(f'Server running on http://0.0.0.0:{port}')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped.')
    finally:
        server.server_close()
