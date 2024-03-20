class Node:
    # def __init__(self, key, value):
    def __init__(self, data):
        self.data = data
        # self.key = key
        # self.value = value
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if data < self.data:
            if not self.left_child:
                self.left_child = Node(data)
            else:
                self.left_child.insert(data)
        else:
            if not self.right_child:
                self.right_child = Node(data)
            else:
                self.right_child.insert(data)

    def search(self, value):
        if value < self.data:
            if self.left_child:
                return self.left_child.search(value)
            else:
                return False
        elif self.data < value:
            if self.right_child:
                return self.right_child.search(value)
            else:
                return False
        else:
            return True

    def print_tree(self):
        if self.left_child:
            self.left_child.print_tree()
        print(self.data)
        if self.right_child:
            self.right_child.print_tree()


# n1 = Node('root node')
# n2 = Node('left node')
# n3 = Node('right node')
# n4 = Node('left grand node')

# n1.left_child = n2
# n1.right_child = n3
# n2.left_child = n4


# cur = n1
# while cur:
#     print(cur.data)
#     cur = cur.left_child

# def preorder(root_node):
#     cur = root_node
#     if cur is None:
#         return
#     print(cur.data)
#     preorder(cur.left_child)
#     preorder(cur.right_child)


# preorder(n1)


# def postorder(root_node):
#     cur = root_node
#     if cur is None:
#         return
#     postorder(cur.left_child)
#     postorder(cur.right_child)
#     print(cur.data)


# postorder(n1)
# def inorder(root_node):
#     cur = root_node
#     if cur is None:
#         return
#     inorder(cur.left_child)
#     print(cur.data)
#     inorder(cur.right_child)


# inorder(n1)

root = Node(12)
root.insert(78)
root.insert(5)
root.insert(7)

# root.print_tree()
print(root.search(7))
