import binascii
import socket

HEADER_SIZE = 40
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 1234

HEADER = '4500 0028 1c46 4000 4006 9D35 C0A8 0003 C0A8 0001'.replace(' ', '')

msg = '434f 4c4f 4d42 4941 2032 202d 204d 4553 5349 2030'.replace(' ', '')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER, PORT))
    msg = HEADER + msg
    s.send(bytes(msg,"utf-8"))
    
    
