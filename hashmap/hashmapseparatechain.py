class Entry:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.hash=hash(key)
    

class HT:
    def __init__(self):
        self.size=0
        self.capacity=5
        self.data=[ [] for i in range(self.capacity)]


    def getsize(self):
        return self.size

    def insert(self,key,value):
        entry=Entry(key,value)
        index=entry.hash % self.capacity

        isUpdated=False


        for i in range(len(self.data(index))):
            if(self.data(index)[i].key==key):
                self.data[index][i]=entry
                isUpdated=True
                break

        if isUpdated==False:
            self.data[index].append(entry)
            self.size +=1

    def remove(key):
        pass


    def get(key):
        index=hash(key) % self.capacity


        for i in range(len):



    def print(self):
        for i in range(self.capacity):
            print("bucket: " str(i)+ ":")
            for e in self.data[i]:
                print(e,sep="->")



hashtable=HT()
hashtable.print()
hashtable.insert("roll no 1 :",123)
hashtable.insert("roll no 2 :",112)
hashtable.insert("roll no  1:",456)



    