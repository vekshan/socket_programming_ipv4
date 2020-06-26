import binascii
import socket


def checksum():
    # TODO
    pass


######### MAIN ###########
HEADER_SIZE = 40
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 1234


# TODO get user input
msg = ""

HEADER = bytes(
    "4500 0028 1c46 4000 4006 0000 C0A8 0003 C0A8 0001".replace(" ", ""), "utf-8"
)  # for testing only, should be done below

msg = "COLOMBIA 2 - MESSI 0"

# encode msg
msg = binascii.hexlify(bytes(msg, "utf-8"))

# calculate total length of IP header, payload + 20 for header, convert to hex
msg_length = "{:04X}".format(len(msg) + 20)

# convert ip addresses to hex
print("You IP Address is: " + SERVER)
IPHex = binascii.hexlify(socket.inet_aton(SERVER)).upper()

# calculate checksum in hex


# concatenate header and convert to bytes


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER, PORT))
    msg = HEADER + msg
    s.send(msg)
