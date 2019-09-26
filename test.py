from packet import *

f=open("a.txt","rb")
data=f.read(100)
print(data)
s="abcdefghijklmnopqrstu".encode()
ss=s.splitlines()
packetData=packet("ACK",5,5,s)
a=packetData.convertToArray()
print(a)
print(a[8]^a[9])