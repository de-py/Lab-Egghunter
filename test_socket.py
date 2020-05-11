import sys
import socket

ip = sys.argv[1]
socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
socket.connect((ip , 33))


while True:
    j = raw_input("Enter: ")
    socket.send(j)
    d = socket.recv(1024)
    print(d)
    if j == "exit":