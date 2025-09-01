import http.server
import socketserver
import webbrowser
import socket

def find_free_port(start_port=8000):
    """Finds an available TCP port, starting from start_port."""
    port = start_port
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port # Port is free
        port += 1

# Find an available port before starting the server
PORT = find_free_port()

Handler = http.server.SimpleHTTPRequestHandler

try:
    # Allow the server to reuse the address to avoid "Address already in use" errors on quick restarts
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        server_url = f"http://localhost:{PORT}"
        print(f"--- Simple web server starting at: {server_url} ---")
        
        # Automatically open the index.html file in a new browser tab
        webbrowser.open_new_tab(f"{server_url}/index.html")
        
        print("\nYour Netflix Recommendation System is now running.")
        print("If it didn't open automatically, please open this URL in your browser:")
        print(f"==> {server_url}/index.html")
        print("\nPress Ctrl+C in this terminal to stop the server.")
        
        # Keep the server running until you stop it
        httpd.serve_forever()

except KeyboardInterrupt:
    print("\nServer stopped by user. Exiting.")
    if 'httpd' in locals():
        httpd.server_close()
except Exception as e:
    print(f"\n[ERROR] Could not start server: {e}")

