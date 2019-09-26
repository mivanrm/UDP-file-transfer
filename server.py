import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_IP ="127.0.0.1"
UDP_PORT =int(input("Masukkan Port yang mau di bind"))
buf = 1024
sock.bind((UDP_IP,UDP_PORT))
print(UDP_IP)
f=open("receive.txt","w")
while True: 
    data,addr=sock.recvfrom(1024)
    print(addr)
    f.write(data.decode('utf-8'))
    print(data.decode())    
    sock.sendto("ack".encode(),addr)
f.close()
