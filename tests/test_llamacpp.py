from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from threading import Thread

import ragvi.generate as generate


def test_llamacpp_sends_fixed_decoding_settings_and_extracts_answer():
    assert hasattr(generate, 'load_llamacpp'), 'Thiếu bộ sinh llama.cpp'
    received = []

    class Handler(BaseHTTPRequestHandler):
        def do_POST(self):
            received.append((self.path, json.loads(self.rfile.read(int(self.headers['Content-Length'])))))
            content = json.dumps({'choices': [{'message': {'content': ' Hà Nội '}}]}).encode()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(content)

    with HTTPServer(('127.0.0.1', 0), Handler) as server:
        worker = Thread(target=server.serve_forever)
        worker.start()
        try:
            infer = generate.load_llamacpp(f'http://127.0.0.1:{server.server_port}', 'test-gguf')
            assert infer('Thủ đô Việt Nam là gì?') == 'Hà Nội'
        finally:
            server.shutdown()
            worker.join()
    assert received == [('/v1/chat/completions', {
        'model': 'test-gguf', 'messages': [{'role': 'user', 'content': 'Thủ đô Việt Nam là gì?'}],
        'temperature': 0, 'seed': 0, 'max_tokens': 256,
    })]
