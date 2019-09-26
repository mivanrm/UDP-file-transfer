import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_IP ="127.0.0.1"
UDP_PORT =8080
buf = 1024
sock.bind((UDP_IP,UDP_PORT))
print(UDP_IP)
f=open("receive.txt","w")
found=True
sock.settimeout(10)
while True and found: 
    data,addr=sock.recvfrom(108)
    if(data):
        f.write(data.decode('utf-8'))
        print(data.decode())    
        sock.sendto("ack".encode(),addr)
    else:
        found=False
print('keluar')
f.close()
