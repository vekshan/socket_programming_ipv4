import binascii
import socket
import sys

# Method for encoding (at the client side):
def calculate_checksum(list_str):
    header_list = list_str.split(" ")
    header_list_hex = [int(i, 16) for i in header_list]
    total = hex(sum(header_list_hex))
    total_list = list(total)[2:]

    if len(total_list) % 4 != 0:
        result = "".join(
            list(hex(int(total_list[0], 16) + int("".join(total_list[1:]), 16)))[2:]
        )
    else:
        result = "".join(total_list)

    return "".join(list(hex(int("FFFF", 16) - int(result, 16))))[2:]


######### MAIN ###########
IPHEADER_SIZE = 40
HEADER_SIZE = 20
DESTINATIONIP = socket.gethostbyname(socket.gethostname())
# DESTINATIONIP = "192.168.0.3"
PORT = 1234

# get user inputs
msg = sys.argv[4]
SOURCEIP = sys.argv[2]

# get data for variable fields in IP Header:
# encode msg
msg = binascii.hexlify(bytes(msg, "utf-8"))

# calculate total length of IP header, payload + 20 for header, convert to hex
total_length_hex = "{:04X}".format((len(msg) // 2) + HEADER_SIZE)

# convert ip addresses to hex
DESTINATIONIP_HEX = binascii.hexlify(socket.inet_aton(DESTINATIONIP), b" ", -2)
SOURCEIP_HEX = binascii.hexlify(socket.inet_aton(SOURCEIP), b" ", -2)

# combine to make the header (initial before encode):
header_str = (
    "4500 "
    + total_length_hex
    + " 1c46 4000 4006 0000 "
    + DESTINATIONIP_HEX.decode("utf-8")
    + " "
    + SOURCEIP_HEX.decode("utf-8")
)

# calculate checksum in hex
checksum = calculate_checksum(header_str)

# concatenate header and convert to bytes
header_str = (
    "4500 "
    + total_length_hex
    + " 1c46 4000 4006 "
    + checksum
    + " "
    + DESTINATIONIP_HEX.decode("utf-8")
    + " "
    + SOURCEIP_HEX.decode("utf-8")
)

ip_header_str = header_str + msg.decode("utf-8")

HEADER = bytes(header_str, "utf-8")

IPHEADER = bytes(ip_header_str.replace(" ", ""), "utf-8")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((DESTINATIONIP, PORT))
    msg = IPHEADER + msg
    s.send(msg)
