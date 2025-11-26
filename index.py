import http.server
import socketserver
import threading
import os

PORT = 3000  # puerto 3000 para evitar conflicto con backend

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

def start_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"✅ Servidor corriendo en http://localhost:{PORT}")
        print(f"📁 Sirviendo archivos desde: {os.getcwd()}")
        httpd.serve_forever()

server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

print("⏳ Servidor frontend iniciado...")
print(f"🌐 Accede al dashboard en: http://localhost:{PORT}")
print(f"📊 Frontend: http://localhost:{PORT}")
print(f"🔧 Backend API: Tu servidor ngrok en puerto 8000")

# Mantener el programa corriendo
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\n🛑 Servidor detenido")
