import binascii
import socket


HEADER_SIZE = 40
SERVER = socket.gethostname()
PORT = 9999


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER, PORT))
    s.listen()
    conn, add = s.accept()
    with conn:
        msg =''
        receiving = True
        while True:
            data = conn.recv(HEADER_SIZE)
            if receiving:
                print(f'new message length:{msg[:HEADER_SIZE]}')
            if not data:
                break
