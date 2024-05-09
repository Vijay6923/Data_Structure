class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
    def __str__(self):
        return str(2*self.data)
class DLL:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0
    def size(self):
        return self.__size
    def isEmpty(self):
        return self.size==0
    def append(self,data):
        newNode=Node(data)
        if (self.isEmpty()):
            self.__head=newNode
            self.__head=newNode
        else:
            self.__tail.next=newNode
            newNode.prev=self.__tail
            self.__tail=newNode
    def __str__(self):
        l1=[]
        trav=self.__head
        while trav is not None:
            l1.append(str(trav,data))
            trav=trav.next
        return "<->".join(l1)
    def addFirst(self,data):
        newNode=Node(data)
        if self.isEmpty():
            self.__head=newNode
            self.__tail=newNode
        else:
            newNode.next=self.__head
            self.__head.prev=newNode
            self.__head=newNode



l=DLL()
print(l.size())
print(l.isEmpty())
l.append(2)
l.append(3)
l.append(1)
print(l.size())
print(l.size())
