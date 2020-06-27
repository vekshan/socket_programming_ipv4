# CEG 3185 Lab #3

Completed by Group #23: Sukhsimranpreet Sekhon (300018861) & Vekshan Bundhoo (300035157)

## Getting Started

### Included Files:

- packet_sender.py
- packet_receiver.py

### Used Technology & Libraries:

- Python Version: 3.8.3   
- - **NOTE:** binascii library will throw an error for a version of python less than 3.8 
- Created on Windows 10 using Visual Studio
- binascii module - Convert between binary and ASCII
- socket - Low-level networking interface
- sys - System-specific parameters and functions

### How To Run Code:

Note: Use two occurences of the same command line tool, such as cmd or git bash, to run both files seperately (in-order to see the client and server relationship).

- On one of the command line tools, run the packet_receiver.py file. For example, if you were using cmd:

```
python packet_receiver.py
```

or

```
py packet_receiver.py
```

- On the second command line tool, run the packet_sender.py file. However, this file needs to take in the server address (destination IP address) and the message that the user wants to send (should be of size 20 bytes) as arguments. For example, if you were using cmd:

```
python packet_sender.py -server 192.168.0.1 -payload "COLOMBIA 2 - MESSI 0"
```

or

```
py packet_sender.py -server 192.168.0.1 -payload "COLOMBIA 2 - MESSI 0"
```

- As you will see, the client will read the data from the user and send the encoded stream to the server through socket. Thereafter, the server will acknowledge the client that the encoded stream has been received, where it decodes the stream and prints it on the screen.
