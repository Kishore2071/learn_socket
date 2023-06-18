import socket as s
from threading import Thread
from time import sleep

"""
GOALS:
------
1.It has to be multithreaded.
2.It has to be group chat.
3.One message has to be delivered to all the connected clients.
4.The server has to take the username before letting him chat.
5.Tell when a person connects,and tell when a person leaves.
6.Message length : 1024.
"""

class chatBotThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.threads = []
        self.messages = []

    def addChatThread(self,thread):
        self.threads.append(thread)

    def queueMessage(self,user,message):
        self.messages.append(message)

    def run():
        while True:
            sleep(0.025)
            if len(self.messages) > 0:
                for thread in self.threads:
                    for message in self.messages:
                        user = message[0]
                        msg = message[1]
                        if thread.getUsername() != user:



class ChatServerOutgoingThread(Thread):
    def __init__(self,incoming_thread):
        Thread.__init__(self)
        self.incoming_thread = incoming_thread
        self.messages = []
        self.can_kill = False

    def sendMessage(self,message):
        fMessage = "{username}: {message}".format(username=self.incoming_thread.getUsername(), message=message)

        try:
            conn = self.incoming_thread.getConnection()
            conn.sendall(fMessage.encode())
        except:
            self.killThread()

    def queueMessage(self,message):
        self.messages.append(message)

    def killThread(self, should_inform = False):
        self.can_kill=True

    def run(self):
        while True:
            sleep(0.1) #100 milliseconds
            if self.can_kill:
                break #if loop break thread has to end.
            if len(self.messages)>0:
                for message in self.messages:
                    try:
                        self.sendMessage(message)
                    except:
                        #inform other that the client has disconnected
                        break


class ChatServerIncomingThread(Thread):
    def __init__(self,conn,addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.username = ""
        self.user_ip = addr[0]
        self.user_port = addr[1]
        self.incoming_thread= None
        self.can_kill = False

    def setUsername(self,username):
        self.username = username

    def getUsername(self):
        return self.username

    def getConnection(self):
        return self.conn

    def isClosed(self):
        return self.conn._closed

    def initSendMessageThread(self,message):
        self.incoming_thread = ChatServerOutgoingThread(self)

    def sendMessage(self,message):
        self.incoming_thread.queueMessage(message)

    def killThread(self):
        self.can_kill=True

    def run(self):
        while not self.conn._closed:
            data = self.conn.recv(1024)
            if not data:
                #inform other that client has disconnected.
                self.incoming_thread.killThread()
                break


HOST = ''
PORT = 9988

bot = ChatBotThread()

sock = s.socket(s.AF_INET, s.SOCK_STREAM)
sock.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen()  # Look for calling bell
while not sock._closed:  # To accept many incoming connections.
    conn, addr = s.accept()  # Open door
    t = ChatServerIncomingThread(conn,addr)
    t.start()
    threads.append(t)

if not sock_closed:
    sock.close()


