import socket
import sys
from packet import *


def checkSum(arraydata):

    check1 = 0
    check2 = 0
    for i in range(8, 108):
        if(i % 2 == 0):
            check1 ^= arraydata[i]
        else:
            check2 ^= arraydata[i]
    check1 ^= (arraydata[0] ^ arraydata[2] ^ arraydata[4])
    check2 ^= (arraydata[1] ^ arraydata[3] ^ arraydata[5])
    return check1, check2


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_IP = "127.0.0.1"
UDP_PORT = 10000
buf = 1024
sock.bind((UDP_IP, UDP_PORT))
print(UDP_IP)
found = True

while True:
    try:
        data, addr = sock.recvfrom(108)
        print(data)
        if(((data[3] << 8)+data[2])==1):
            filename=bytes(data[8:108]).decode().rstrip('\0')+"_receive1.txt"
            print(filename)
            f = open(filename, "wb")   
        else:
            f.write((bytes(data[8:108]).decode().rstrip('\0')).encode())
            print("Packet ke"+str(((data[3] << 8)+data[2])))
            print("File ke"+str(data[1]))
        if((data[6], data[7]) == (checkSum(data))):
            ackPacket = packet("ACK", data[1], (data[3] << 8+data[2]), '')
            sock.sendto(ackPacket.getPacketArray(), addr)
        print("last")
    except KeyboardInterrupt:
        break
print('keluar')
f.close()
