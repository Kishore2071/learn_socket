import socket

HOST = ''
PORT = 3074

name = input("Enter your name: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    # AF - Address Family
                    # INET - Internet
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.connect((HOST,PORT))

while(True):
    msg = input("Message: ")
    if(msg == "quit"):
        break
    msg = name + ": " + msg
    s.send(msg.encode())
s.close()