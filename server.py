from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]
        # Ensuring access is only allowed from VPN-assigned IP addresses
        if not client_ip.startswith('10.8.0.'):
            self.send_error(403, "Access Denied: Not on VPN")
            return

        # Redirecting /redirect to the homepage
        if self.path == '/redirect':
            self.send_response(302)
            self.send_header('Location', '/')
            self.end_headers()
            return

        # Serving the requested file
        elif self.path == '/':
            self.path = '/index.html'

        # Handling non-existing paths with a custom 404 page
        elif not os.path.exists(self.path[1:]):  # skip the leading '/'
            self.send_error(404, "File not found.")
            return

        return SimpleHTTPRequestHandler.do_GET(self)

    def send_error(self, code, message=None):
        # Use a custom HTML template for 404 errors
        if code == 404:
            self.error_message_format = open('404.html').read()
        return SimpleHTTPRequestHandler.send_error(self, code, message=message)

def run(server_class=HTTPServer, handler_class=CustomHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
