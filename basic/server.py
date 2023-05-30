import socket

HOST= ''
PORT= 1234

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((HOST,PORT))
s.listen()

conn,addr = s.accept()

print('client connected: ', addr)

while True:
    data=conn.recv(1024)
    print("client input:" + data.decode())
    if not data:
        break
    elif data.decode()=="quit":
        print("Exiting...")
        break

conn.close()
s.close()