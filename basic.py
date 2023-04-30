import socket

HOST = ''
PORT = 3074

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # AF - Address Family
                # INET - Internet

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
while (True):
    conn, addr = s.accept()
    # conn - the connection object with the client
    # addr - array 0 - IP address of the client
    #		array 1 - The back port with which the connection is established
    print("IP {} connected".format(addr[0]))
    print(addr)
    conn.sendall(b"Hello, welcome to this workshop")
    conn.close()
s.close()
