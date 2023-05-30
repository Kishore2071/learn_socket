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
    data= data.decode()
    print("client input:" + data)
    if not data:
        break
    elif data=="quit":
        print("Exiting...")
        break
    else:
        data = data + 'Data changes by server'
        s.sendall(data.encode())
conn.close()
s.close()