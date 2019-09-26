class packet:
    def __init__(self, TYPE, ID, SEQ_NUMBER, DATA):
        self.packetArray=bytearray(32776)
        if(TYPE=="DATA"):
            self.packetArray[0]=0x0 &255
        elif(TYPE=="ACK"):
            self.packetArray[0]=0x1&255
        elif(TYPE=="FIN-ACK"):
            self.packetArray[0]=0x2&255
        elif(TYPE=="FIN"):
            self.packetArray[0]=0x3&255        
        LENGTH = len(DATA)
        
        self.packetArray[1]=ID &255
        self.packetArray[2]=SEQ_NUMBER&255
        self.packetArray[3]=SEQ_NUMBER>>8&255
        self.packetArray[4]=LENGTH &255
        self.packetArray[5]=LENGTH>>8&255
        i=8
        self.packetArray[6]=0
        self.packetArray[7]=0
        j=8
        print(len(DATA))
        for b in DATA:
            self.packetArray[j]=b
            j+=1
        for i in range(8,32775):
            
            if(i%2==0):
                self.packetArray[6]^=self.packetArray[i]
            else:
                self.packetArray[7]^=self.packetArray[i]
            i+=1
        self.packetArray[6]^=(self.packetArray[0]^self.packetArray[2] ^self.packetArray[4])
        self.packetArray[7]^=(self.packetArray[1]^self.packetArray[3] ^self.packetArray[5])

    def getPacketArray(self):
        return self.packetArray
    def getType(self):
        return self.packetArray[0]
    def getID(self):
        return self.packetArray[1]
    def getSeqNumber(self):
        return ((self.packetArray[3]<<8)+self.packetArray[2])
    def getLength(self):
        return ((self.packetArray[5]<<8)+self.packetArray[4])
    def setType(self,TYPE):
        if(TYPE=="DATA"):
            self.packetArray[0]=0x0 &255
        elif(TYPE=="ACK"):
            self.packetArray[0]=0x1&255
        elif(TYPE=="FIN"):
            self.packetArray[0]=0x2&255
        elif(TYPE=="FIN-ACK"):
            self.packetArray[0]=0x3&255   
        self.packetArray[6]=0
        self.packetArray[7]=0
        for i in range(8,32775):
            
            if(i%2==0):
                self.packetArray[6]^=self.packetArray[i]
            else:
                self.packetArray[7]^=self.packetArray[i]
            i+=1
        self.packetArray[6]^=(self.packetArray[0]^self.packetArray[2] ^self.packetArray[4])
        self.packetArray[7]^=(self.packetArray[1]^self.packetArray[3] ^self.packetArray[5])

