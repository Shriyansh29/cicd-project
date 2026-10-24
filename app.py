from http.server import BaseHTTPRequestHandler, HTTPServer

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = b"CI/CD Pipeline is Working!"

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(message)))
        self.end_headers()
        self.wfile.write(message)

server = HTTPServer(("0.0.0.0", 8000), AppHandler)
print("Application running on port 8000")
server.serve_forever()
