class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
    def __str__(self):
        return str(2*self.data)
node=Node(10)
print(node)
print(node.data)