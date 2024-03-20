class Node:
    def __init__(self, data=None, next_item=None, prev=None):
        self.data = data
        self.next = next_item
        self.prev = prev


class DuoList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def add_end(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.counter += 1

    def add_begin(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.counter += 1

    def insert_in_l(self, data, position):
        node = Node(data)
        cur_pos = self.head
        next_pos = cur_pos.next
        cnt = 0
        while cur_pos:
            if cnt == position:
                node.next = next_pos
                node.prev = cur_pos
                cur_pos.next = node
                next_pos.prev = node
                break

            cur_pos = cur_pos.next
            next_pos = cur_pos.next
            cnt += 1
        self.counter += 1

    def del_from_l(self, position):
        cur_pos = self.head
        next_pos = None
        prev_pos = None
        cnt = 0
        while cur_pos:
            if cnt == position:
                prev_pos.next = next_pos
                # next_pos.prev = cur_pos.prev
                next_pos.prev = prev_pos
                break
            cur_pos = cur_pos.next
            next_pos = cur_pos.next
            prev_pos = cur_pos.prev
            cnt += 1
        self.counter -= 1

    def del_from_tail(self):
        # if cnt == 1:
        #     self.head = None
        #     self.tail = None
        tmp = self.tail.prev
        tmp.next = None
        self.tail = tmp
        self.counter -= 1

    def del_from_head(self):
        tmp = self.head.next
        tmp.prev = None
        self.head = tmp
        self.counter -= 1

    def printer_lr(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
        print(self.counter, 'длина списка')

    def printer_rl(self):
        cur = self.tail
        while cur:
            print(cur.data, end=' ')
            cur = cur.prev


ll = DuoList()
ll.add_end('f')
ll.add_end('u')
ll.add_end('c')
ll.add_end('k')
ll.insert_in_l('g', 2)
ll.printer_lr()
print()
# ll.del_from_tail()
# ll.printer_lr()
print()
# ll.del_from_head()
# ll.printer_lr()
ll.del_from_l(3)
ll.printer_lr()
# ll.printer_lr()
# print()
# ll.add_begin(0)
# ll.printer_lr()
# print()
# ll.printer_rl()
