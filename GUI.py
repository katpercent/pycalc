import sys
import http.server
import socketserver
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtWebEngineWidgets import QWebEngineView
import threading
import os
import socket

PORT = 8000
dir_path = os.path.dirname(os.path.realpath(__file__))

class HttpServerThread(threading.Thread):
    def run(self):
        try:
            # Create socket
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind(('127.0.0.1', PORT))
            server.listen(1)
            print("Test 1 passed")
            
            while True:    
                # Wait for client connections
                client_connection, client_address = server.accept()
                # Get the client request
                request = client_connection.recv(1024).decode()
                # Get the content of calc.html
                html = open(dir_path+'/dir/calc.html')
                content = html.read()
                html.close()

                # Send HTTP response
                # IP of the client print(client_address[0])
                response = 'HTTP/1.0 200 OK\n\n' + content
                client_connection.sendall(response.encode())
                client_connection.close()
                break
        except Exception as e:
            print("Test 1 failed because",e)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            self.setGeometry(100, 100, 400, 550)
            self.setWindowIcon(QIcon(dir_path+'/dir/icon.ico'))
            self.setWindowTitle("Calculator by kgbcyber")
            self.webview = QWebEngineView()
            self.setCentralWidget(self.webview)
            self.load_page()
            print("Test 3 passed")
        except Exception as e:
            print("Test 3 failed because",e)

    def load_page(self):
        try:
            url = QUrl("http://localhost:{}/calc.html".format(PORT))
            self.webview.load(url)
            print("Test 2 passed")
        except Exception as e:
            print("Test 2 failed because",e)

if __name__ == "__main__":
    # Start the HTTP server in a separate thread
    http_server = HttpServerThread()
    http_server.start()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
        