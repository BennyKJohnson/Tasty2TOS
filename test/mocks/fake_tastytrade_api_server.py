from http.server import BaseHTTPRequestHandler, HTTPServer
from test.mocks.tastytrade_api_mock_responses import get_wmt_equity_option_chain_response_body, get_es_futures_option_chain_response_body
import json

class FakeTastyTradeApiServer:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.http_server = HTTPServer((host, port), lambda request, client_address, server: FakeTastyTradeApiHTTPRequestHandler(request, client_address, self))
        self.last_request = None

    def start(self):
        self.http_server.serve_forever()

    def stop(self):
        self.http_server.shutdown()
        self.http_server.server_close()

    def handle_request(self, request):
        self.last_request = request
        if request['method'] == 'POST' and request['path'] == '/sessions':
            return self.handle_create_session(request)
        elif request['method'] == 'GET' and request['path'] == '/option-chains/WMT/nested':
            return self.handle_get_wmt_equity_option_chain(request)
        elif request['method'] == 'GET' and request['path'] == '/futures-option-chains/ES/nested':
            return self.handle_get_es_futures_option_chain(request)
        
    def handle_get_wmt_equity_option_chain(self, request):
        return get_wmt_equity_option_chain_response_body()
    
    def handle_create_session(self, request):
        return {
            'data': {
                'session-token': 'SESSION_TOKEN',
            }
        }

    def handle_get_es_futures_option_chain(self, request):
        return get_es_futures_option_chain_response_body()

class FakeTastyTradeApiHTTPRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server) -> None:
        self.server = server
        super().__init__(request, client_address, server)

    def do_POST(self):
        post_paths = [
            '/sessions'
        ]

        if self.path in post_paths:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            response_data = self.server.handle_request({
                'body': data,
                'method': 'POST',
                'path': self.path,
                'headers': self.headers
            })
            response_body = json.dumps(response_data).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Content-length', len(response_body))
            self.end_headers()
            self.wfile.write(response_body)
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        get_paths = [
            '/option-chains/WMT/nested',
            '/futures-option-chains/ES/nested'
        ]
        if self.path in get_paths:
            response_data = self.server.handle_request({
                'method': 'GET',
                'path': self.path,
                'headers': self.headers
            })
            response_body = json.dumps(response_data).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Content-length', len(response_body))
            self.end_headers()
            self.wfile.write(response_body)
        else:
            print('NOT FOUND GET', self.path)
            self.send_response(404)
            self.end_headers()
