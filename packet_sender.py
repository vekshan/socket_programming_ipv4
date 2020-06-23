import binascii
import socket

HEADER_SIZE = 40
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 1234

HEADER = '450000281c46400040069D35C0A80003C0A80001'
msg = "works"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER, PORT))
    msg = f'{len(msg):<{HEADER_SIZE}}'+ msg
    s.sendall(b'Hello, world')
    
    
