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

    def inserter(self, data, position=None):
        node = Node(data)
        # add to end
        if position == -1:
            if self.tail is None:
                self.head = node
                self.tail = node
                self.counter += 1
                return
            elif self.tail:
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
                self.counter += 1
                return

        # add to begin
        if position == 0:
            if self.head is None:
                self.head = node
                self.tail = node
                self.counter += 1
                return
            elif self.head:
                node.next = self.head
                self.head.prev = node
                self.head = node
                self.counter += 1
                return

        # add inside
        position -= 1
        cnt, inc_dec = DuoList.find_closest_position(self.counter, position)
        if inc_dec < 0:
            cur_pos = self.tail
        else:
            cur_pos = self.head
            next_pos = cur_pos.next

        while cur_pos:
            if cnt == position:
                if cnt == position:
                    node.next = next_pos
                    node.prev = cur_pos
                    cur_pos.next = node
                    next_pos.prev = node
                    self.counter += 1
                    break
            if inc_dec > 0:
                cur_pos = cur_pos.next
                next_pos = cur_pos.next
                cnt += 1
            else:
                next_pos = cur_pos
                cur_pos = cur_pos.prev
                cnt -= 1

    def remover(self, position):
        if position in [-1, self.counter]:
            # remove from tail
            tmp = self.tail.prev
            tmp.next = None
            self.tail = tmp
            self.counter -= 1
        elif position == 0:
            # remove from head
            tmp = self.head.next
            tmp.prev = None
            self.head = tmp
            self.counter -= 1
        else:
            # remove from inside
            next_pos = None
            prev_pos = None
            cnt, inc_dec = DuoList.find_closest_position(self.counter, position)
            if inc_dec < 0:
                cur_pos = self.tail
            else:
                cur_pos = self.head
            while cur_pos:
                if cnt == position:
                    prev_pos.next = next_pos
                    next_pos.prev = prev_pos
                    break
                if inc_dec > 0:
                    cur_pos = cur_pos.next
                    next_pos = cur_pos.next
                    prev_pos = cur_pos.prev
                    cnt += 1
                else:
                    next_pos = cur_pos
                    cur_pos = cur_pos.prev
                    prev_pos = cur_pos.prev
                    cnt -= 1
            self.counter -= 1

    def printer_lr(self):
        cur = self.head
        while cur:
            print(cur.data, end='')
            cur = cur.next
        print()
        print(f'Len of the list: {self.counter}')

    @classmethod
    def find_closest_position(cls, len_of_list, position):
        mid_pos = round(len_of_list / 2)
        if position <= mid_pos:
            return 0, 1
        elif mid_pos < position:
            return len_of_list, -1


ll = DuoList()
for i in 'Test text':
    ll.inserter(i, -1)
ll.printer_lr()
print()
# ll.remover(int(input(f'Enter a num of position to delete: ')))
# ll.printer_lr()
ll.inserter(input(f'Enter an element: '), int(input(f'Enter a num of position: ')))
ll.printer_lr()
input()
