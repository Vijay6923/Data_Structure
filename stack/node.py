class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Stack:
    def __init__(self):
        self.__size=0
        self.__head=None

def size(self):
    return  self.__size
def isEmpty(self):
    return (self.size()==0)
def push(self,val):
    newNode=Node(val)
    self.head=newNode
    




def pop(self):
    if self.isEmpty():
        raise Exception("stack overflow")
    data=self.__head.__data
    temp=self.__head
    self.head=self.head.node
