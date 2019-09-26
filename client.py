import socket
import select
from packet import *

UDP_IP = "127.0.0.1"
IN_PORT = 5005
Address=(input("Masukkan Address pengiriman")).split(":")
print(Address[0])
print(int(Address[1]))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
timeout = 3
seq_number=1
textfile="testing"
filename=input("masukkan nama file")
f=open(filename,"rb")
data=f.read(100)
while data:
    sendData=packet("DATA",0,seq_number,data)
    datalist=sendData.convertToArray()
    print(datalist)
    sock.sendto(datalist,(Address[0],int(Address[1])))
    ackValidation=sock.recvfrom(1024)
    print(ackValidation[0].decode())
    data=f.read(100)
f.close()