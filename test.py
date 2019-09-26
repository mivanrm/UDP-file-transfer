from packet import *

f=open("a.txt","rb")
data=f.read(100)
print(data)
s="abcd".encode()
ss=s.splitlines()
print(s)
for x in s :
    print(x)
packetData=packet("ACK",5,5,'data'.encode())
a=packetData.convertToArray()
print(a)