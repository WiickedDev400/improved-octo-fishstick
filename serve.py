import argparse
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

ROOT = Path(__file__).resolve().parent

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Serve the local repository over HTTP.")
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", 8000)), help="Port to serve on")
    args = parser.parse_args()

    server_address = ("", args.port)
    httpd = HTTPServer(server_address, Handler)
    print(f"Serving {ROOT / 'index.html'} at http://127.0.0.1:{args.port}")
    print("Press Ctrl+C to stop.")
    httpd.serve_forever()
