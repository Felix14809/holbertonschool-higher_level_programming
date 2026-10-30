#!/usr/bin/env python3
"""program that creates a simple local http server"""
import http.server
import json


class httphandler(http.server.BaseHTTPRequestHandler):
    """handles the http get requests"""

    def send_all(self, status, type, text):
        """Function for reduce repeated code and bloat when sending"""
        self.send_response(status)
        self.send_header("content-type", type)
        self.end_headers()
        self.wfile.write(text.encode("utf-8"))

    def do_GET(self):
        if self.path == "/":
            self.send_all(200, "plain/text", "Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_all(200, "application/json", json.dumps(data))
        elif self.path == "/status":
            self.send_all(200, "plain/text", "OK")
        elif self.path == "/info":
            info = {"version": "1.0", "description":
                    "A simple API built with http.server"}
            self.send_all(200, "application/json", json.dumps(info))
        else:
            self.send_all(404, "text/plain", "Endpoint not found")


if __name__ == "__main__":
    server = http.server.HTTPServer(("", 8000), httphandler)
    server.serve_forever()
