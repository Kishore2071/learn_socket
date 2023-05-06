import socket

HOST = ''    # all available interfaces
PORT = 1234  # any port > 1023
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)  # 1 means the number of accepted connections
conn, addr = s.accept()  # waits for a new connection
print('Client connected: ', addr)
while True:
    data = conn.recv(1024)
    print("clients input: " + data.decode())
    if not data:
        break
    elif data.decode()=="quit":
        print("Exiting...")
        break
    else:
        data = data.decode()+"change by server"
        conn.sendall(data.encode())
conn.close()
s.close()