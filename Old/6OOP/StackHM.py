class SteckMaker:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size
        self.top = -1

    def push(self, x):
        try:
            self.top += 1
            self.data[self.top] = x
        except IndexError as mesER:
            print(f'{mesER}')

    def pop(self):
        try:
            self.top -= 1
            return self.data[self.top + 1]
        except IndexError as mesER:
            print(f'{mesER}')

    def peek(self):
        if self.top == -1:
            return 'empty'
        else:
            return self.data[self.top]


st_one = SteckMaker(16)
test_line = '([)]'
test_line1 = '{[()]}'

open_list = '({['
close_list = ')}]'

for i in test_line:
    if i in '([{':
        st_one.push(i)
        continue

    if i in ')]}':
        if st_one.peek() == 'empty':
            exit(input('Не збалансовано'))
        close_ind = close_list.index(i)

        if open_list.index(st_one.pop()) != close_ind:
            exit(input('Не збалансовано'))

if st_one.peek() == 'empty':
    print('Повністю збалансований')
else:
    print(f'{st_one.peek()} не збалансована')
