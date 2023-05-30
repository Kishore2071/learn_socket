import socket

HOST = ''
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((HOST, PORT))
print('Client connected.')

while True:
    user_input = str(input())
    if not user_input:
        break
    else:
        s.sendall(user_input.encode())

s.close()