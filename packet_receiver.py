import binascii
import socket

######### MAIN ###########
HEADER_SIZE = 40
SERVER = socket.gethostname()
PORT = 1234


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER, PORT))
    s.listen()
    conn, add = s.accept()
    with conn:
        msg = ""
        receiving = True
        msg_length = 0
        while True:
            # should be either message size or header size to fix
            data = conn.recv(HEADER_SIZE)
            if receiving:
                msg_length = int(data[4:8], 16)
                print(f"new message length:{msg_length}")
                receiving = False
            msg += data.decode("utf-8")

            if len(msg) - HEADER_SIZE == msg_length:
                print(msg)
                break
