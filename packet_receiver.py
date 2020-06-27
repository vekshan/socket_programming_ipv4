import binascii
import socket


def verify_checksum(msg):
    header_str = msg[:40]  # 0..39 is the header
    header_list = [
        header_str[i : i + 4] for i in range(0, len(header_str), 4)
    ]  # seperate into 4 bits and put in array
    header_list_hex = [int(i, 16) for i in header_list]  # convert each to hex
    total = hex(sum(header_list_hex))  # sum
    total_list = list(total)[2:]  # hex value

    if len(total_list) % 4 != 0:
        result = "".join(
            list(hex(int(total_list[0], 16) + int("".join(total_list[1:]), 16)))[2:]
        )
    else:
        result = "".join(total_list)

    return (
        int("".join(list(hex(int("FFFF", 16) - int(result, 16))))[2:]) == 0
    )  # return true if checksum is 0


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
            data = conn.recv(HEADER_SIZE * 2)
            if receiving:
                msg_length = int(data[4:8], 16) * 2
                # print(f"new message length:{msg_length}")
                # print(data)
                receiving = False
            msg += data.decode("utf-8")

            if len(msg) == msg_length:
                # print(verify_checksum(msg))
                # print(msg)
                break


if verify_checksum(msg) == True:
    msg_list = [msg[i : i + 4] for i in range(0, len(msg), 4)]
    ip = (
        str(int(msg_list[6][:2], 16))
        + "."
        + str(int(msg_list[6][2:], 16))
        + "."
        + str(int(msg_list[7][:2], 16))
        + "."
        + str(int(msg_list[7][2:], 16))
    )
    total_length = int(msg_list[1], 16)
    payload = binascii.unhexlify(bytes(msg[40:], "utf-8")).decode("utf-8")
    data_length = str(total_length - HEADER_SIZE)
    data_length_bit = str((total_length - HEADER_SIZE) * 8)
    print(
        """
            The data received from {0} is {1}
            The data has {2} bits or {3} bytes. Total length of the packet is {4} bytes.
            The verification of the checksum demonstrates that the packet received is correct.
    """.format(
            ip, payload, data_length_bit, data_length, str(total_length)
        )
    )
else:
    print(
        "The verification of the checksum demonstrates that the packet received is corrupted. Packet discarded!"
    )
