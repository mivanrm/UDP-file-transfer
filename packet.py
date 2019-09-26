class packet:
    def __init__(self, TYPE, ID, SEQ_NUMBER, DATA):
        if(TYPE=="DATA"):
            self.packetType=0x0
        elif(TYPE=="ACK"):
            self.packetType=0x1
        elif(TYPE=="FIN-ACK"):
            self.packetType=0x2
        elif(TYPE=="FIN"):
            self.packetType=0x3
        self.ID = ID
        self.SEQ_NUMBER = SEQ_NUMBER
        self.LENGTH = len(DATA)
        self.DATA = DATA

    def convertToArray(self):
        packetArray=bytearray(200+8)
        packetArray[0]=self.packetType &255
        packetArray[1]=self.ID &255
        packetArray[2]=self.SEQ_NUMBER&255
        packetArray[3]=self.SEQ_NUMBER>>8&255
        packetArray[4]=self.LENGTH &255
        packetArray[5]=self.LENGTH>>8&255
        i=8

        for b in self.DATA:
            packetArray[i]=b
            i=+1
            print(b.to_bytes())

        print(i)
        return packetArray
