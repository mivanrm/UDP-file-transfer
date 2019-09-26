import socket
import select
from packet import *

UDP_IP = "127.0.0.1"
IN_PORT = 10000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
timeout = 3

ID = 1
filename = []
packetList=[]
fileNumber = int(input("Masukkan Jumlah file"))
for i in range(fileNumber):
    filename.append(input("masukkan nama file"))
for name in filename:
    seq_number = 1
    namesplit = name.split(".")
    f = open(name, "rb")
    
    data = f.read(100)
    while data:
        if(seq_number == 1):
            Data = packet("DATA", ID, seq_number, namesplit[0].encode())
            packetList.append(Data)
            seq_number += 1
        else:
            Data = packet("DATA", ID, seq_number, data)
            packetList.append(Data)
            seq_number+=1
            data=f.read(100)
        
    ID += 1
print("panjang"+str(len(packetList)))
for i in range(len(packetList)):
    if(i==len(packetList)-1):
        packetList[i].setType("FIN")
    sock.sendto(packetList[i].getPacketArray(),(UDP_IP,IN_PORT))
    

    