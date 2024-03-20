

# 0 - BigBoss, 1 - OfficeWorker, 2 - RandomUser
from datetime import datetime


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

    def enqueue_p(self, data):
        if self.count != self.maxsize:
            self.items.append(data)
            self.count += 1
            self.items.sort(key=lambda x: x.priority)

        else:
            print('Queue is full!!!')

    def dequeue_f(self):
        return self.items.pop(0)

    def print_queue(self):
        for item in self.items:
            print(item.data)


class Printer(Queue):
    def in_queue(self, data, priority):
        priority_list = {'BigBoss': 0, 'OfficeWorker': 1, 'RandomUser': 2}
        super().enqueue_p(Node(data, priority_list[priority]))


class Statistic(Queue):
    def in_queue(self, data):
        super().enqueue_p(Node(data, 0))

    def print_stat(self):
        for item in self.items:
            user = list(item.data.keys())
            time_access = list(item.data.values())
            print(f'{time_access[0]} -> {user[0]}')


n = 8
queue = Printer(n)
print_statistics = Statistic(n)
access_list = ['BigBoss', 'OfficeWorker', 'RandomUser']
print(f'Users with access:')
for i in access_list:
    print(i, end=' ')
print(f'\nFor end the program type EXIT to user code')
while True:
    pr = input(f'Enter a user code: ')
    if pr.lower() == 'exit':
        break
    if pr not in access_list:
        pr = input(f'Can`t find this user, try again: ')
    dt = input(f'Enter a message to print:\n')
    cur_time = datetime.now()
    print_statistics.in_queue({pr: f'{cur_time:%H:%M:%S}'})

    queue.in_queue(dt, pr)

choice = input('Print STATISTIC?'
               '\nY/N: ')
if 'y' in choice.lower():
    print_statistics.print_stat()
queue.print_queue()
