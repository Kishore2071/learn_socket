import socket as s
from threading import Thread

HOST = ''
PORT = 9988

sock = s.socket(s.AF_INET, s.SOCK_STREAM)
sock.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen()  # Look for calling bell
while not sock._closed:  # To accept many incoming connections.
    conn, addr = s.accept()  # Open door

if not sock_closed:
    sock.close()


