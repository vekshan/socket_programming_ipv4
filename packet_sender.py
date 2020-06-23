import binascii
import socket


SERVER = socket.gethostbyname(socket.gethostname())
PORT = 9999


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER, PORT))
    s.sendall(b'Hello, world')
    
    