import binascii
import socket
import sys


def checksum():
    # TODO
    pass


######### MAIN ###########
PACKET_SIZE = 40
HEADER_SIZE = 20
DESTINATIONIP = socket.gethostbyname(socket.gethostname())
SOURCEIP = sys.argv[2]
PORT = 1234

# TODO get user input
msg = sys.argv[4]

# get data for variable fields in IP Header:
# encode msg
msg = binascii.hexlify(bytes(msg, "utf-8"))

# calculate total length of IP header, payload + 20 for header, convert to hex
total_length_hex = "{:04X}".format((len(msg) // 2) + HEADER_SIZE)

# convert ip addresses to hex
DESTINATIONIP_HEX = binascii.hexlify(socket.inet_aton(DESTINATIONIP))
SOURCEIP_HEX = binascii.hexlify(socket.inet_aton(SOURCEIP))

# combine to make IP header (initial before encode):
header_str = (
    "4500 "
    + total_length_hex
    + " 1c46 4000 4006 0000 "
    + DESTINATIONIP_HEX.decode("utf-8")
    + SOURCEIP_HEX.decode("utf-8")
    + msg.decode("utf-8")
)

HEADER = bytes(header_str.replace(" ", ""), "utf-8")

print(HEADER)

# calculate checksum in hex

# concatenate header and convert to bytes

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((DESTINATIONIP, PORT))
    msg = HEADER + msg
    s.send(msg)
