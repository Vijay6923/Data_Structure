class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right 

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root

new_node = Node(13)

root = new_node
root = new_node.insert(root, 10)
root = new_node.insert(root, 15)


def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)

in_order_traversal(root)  
