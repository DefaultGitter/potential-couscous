class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class MyList:
    def __init__(self):
        self.head = None
        self.tail = None

    def ex_add(self, data):
        node = Node(data)  # 1
        if self.tail:  # 3
            self.tail.next = node
            self.tail = node
        else:  # 2
            self.head = node
            self.tail = node

    def my_iter(self):
        current = self.head
        while current:
            tmp = current.data
            current = current.next
            yield tmp

    def printer(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


ll = MyList()
ll.ex_add(5)
ll.ex_add('he-he')
ll.printer()

# for i in ll.my_iter():
#     print(i)
# for i in ll.my_iter():
#     print(i)

# def test():
#     for i in [1, 5, 9, 7, 6, 3, 4]:
#         yield i
#
#
# v1 = test()
# print(v1)

