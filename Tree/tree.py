class Node:
    def __init__(self,data,left,right,parent):
        self.data=data
        self.left=left
        self.right=right
        self.parent=parent

        
class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def add_left_child(self, parent_data, child_data):
        parent_node = self._find(self.root, parent_data)
        if parent_node is None:
            raise ValueError(f"Parent node with data {parent_data} not found")
        if parent_node.left is not None:
            raise ValueError(f"Parent node {parent_data} already has a left child")
        parent_node.left = Node(child_data, parent=parent_node)

    def add_right_child(self, parent_data, child_data):
        parent_node = self._find(self.root, parent_data)
        if parent_node is None:
            raise ValueError(f"Parent node with data {parent_data} not found")
        if parent_node.right is not None:
            raise ValueError(f"Parent node {parent_data} already has a right child")
        parent_node.right = Node(child_data, parent=parent_node)

    def _find(self, node, data):
        if node is None:
            return None
        if node.data == data:
            return node
        left_result = self._find(node.left, data)
        if left_result:
            return left_result
        return self._find(node.right, data)

    def in_order_traversal(self, node, visited):
        if node:
            self.in_order_traversal(node.left, visited)
            visited.append(node.data)
            self.in_order_traversal(node.right, visited)

    def pre_order_traversal(self, node, visited):
        if node:
            visited.append(node.data)
            self.pre_order_traversal(node.left, visited)
            self.pre_order_traversal(node.right, visited)

    def post_order_traversal(self, node, visited):
        if node:
            self.post_order_traversal(node.left, visited)
            self.post_order_traversal(node.right, visited)
            visited.append(node.data)
