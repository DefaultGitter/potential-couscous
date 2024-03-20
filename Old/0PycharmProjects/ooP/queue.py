class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __str__(self):
        return f'{self.data} -> {self.priority}'


class Queue:
    def __init__(self, maxsize):
        self.items = []
        self.maxsize = maxsize
        self.count = 0
        self.i = 0

    def enqueue(self, data):
        if self.count != self.maxsize:
            self.items.append(data)
            self.count += 1
            self.items.sort(key=lambda x: x.priority, reverse=True)

        else:
            print('Queue is full!!!')

    def dequeue_p(self):
        max_p = self.items[0].priority
        max_ind = 0
        ind = 0
        for item in self.items:
            if item.priority > max_p:
                max_p = item.priority
                max_ind = ind

            ind += 1
        return self.items.pop(max_ind)

    def dequeue_c(self):
        tmp = self.items[self.i]
        self.i += 1
        # if self.i == self.maxsize:          # лучше привязка к реальному сайзу
        if self.i == self.count:
            self.i = 0
        return tmp

    def dequeue_f(self):
        return self.items.pop(0)

    def print_queue(self):
        for item in self.items:
            print(item.data, item.priority)


queue = Queue(5)
queue.enqueue(Node('HEHE1', 3))
queue.enqueue(Node('HEHE2', 2))
queue.enqueue(Node('HEHE3', 1))
queue.enqueue(Node('HEHE4', 3))

# print(queue.dequeue_p().priority)
# print(queue.dequeue_p())
# queue.print_queue()
# print(queue.dequeue_c())
# print(queue.dequeue_c())
# print(queue.dequeue_c())
# print(queue.dequeue_c())
# print(queue.dequeue_c())
