import socket

HOST = ''
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((HOST, PORT))
print('Client connected.')

while True:
    user_input = str(input())  # convert input to string
    if not user_input:  # i.e. enter key pressed
        break
    else:
        s.sendall(user_input.encode())  # encode needed to transform string to bytes

s.close()