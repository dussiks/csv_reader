import http.server
import socketserver


PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
server = socketserver.TCPServer(("", PORT), Handler)


if __name__ == '__main__':
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.socket.close()


