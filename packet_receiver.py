import binascii
import socket


def verify_check_sum(msg):
    header_str = msg[:20] #0..19 is the header
    header_list = [header_str[i:i+4] for i in range(0, len(header_str), 4)] #seperate in 4 bits in put in array
    header_list_hex = [int(i, 16) for i in header_list] #convert each to hex
    total = hex(sum(header_list_hex)) #sum 
    total_list = list(total)[2:] #hex value

    if len(total_list) % 4 != 0: 
        result = "".join(
            list(hex(int(total_list[0], 16) +
                     int("".join(total_list[1:]), 16)))[2:]
        )
    else:
        result = "".join(total_list)

    return int("".join(list(hex(int("FFFF", 16) - int(result, 16))))[2:]) == 0 # return true if checksum is 0


######### MAIN ###########
HEADER_SIZE = 20
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

