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

    def remove(self, root, data):
        if root is None:
            return root
        if data < root.data:
            root.left = self.remove(root.left, data)
        elif data > root.data:
            root.right = self.remove(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_larger_node = self.get_min(root.right)
            root.data = min_larger_node.data
            root.right = self.remove(root.right, min_larger_node.data)
        return root

    def get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)

root = Node(13)

root = root.insert(root, 10)
root = root.insert(root, 15)

in_order_traversal(root)
print()

root = root.remove(root, 10)

in_order_traversal(root)
print()