import random


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if data < self.data:
            if not self.left_child:
                self.left_child = Node(data)
                print(f'new[{data}] < root[{self.data}]')
            else:
                self.left_child.insert(data)
        elif data > self.data:
            if not self.right_child:
                self.right_child = Node(data)
                print(f'root[{self.data}] < new[{data}]')
            else:
                self.right_child.insert(data)
        else:
            print(f'{data} already exist')

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
        print(self.data, end=' ')
        if self.right_child:
            self.right_child.print_tree()

    def print_tree_rev(self):
        if self.right_child:
            self.right_child.print_tree_rev()
        print(self.data, end=' ')
        if self.left_child:
            self.left_child.print_tree_rev()

    def tree_height(self, th=1, th_max=1):
        if self.left_child:
            th_max = self.left_child.tree_height(th + 1, th_max)
        if self.right_child:
            th_max = self.right_child.tree_height(th + 1, th_max)
        th_max = max(th_max, th)
        return th_max

    def min_max(self, min_num, max_num=None):
        if max_num is None:
            max_num = min_num
        if self.left_child:
            min_num, max_num = self.left_child.min_max(min_num, max_num)
        if self.right_child:
            min_num, max_num = self.right_child.min_max(min_num, max_num)
        return min(self.data, min_num), max(self.data, max_num)


choice = input(f'Use TEST tree or RANDOM?\n')
match choice.lower():
    case 'test':
        test_tree = [5, 9, 1, 7, 10, 0, 4, 8, 3, 2]  # height might be 6
        root = Node(6)
        print(f'Root[{root.data}]')
        for i in test_tree:
            root.insert(i)
    case 'random':
        root = Node(random.randint(-10, 10))
        print(f'Root[{root.data}]')
        for i in range(random.randint(5, 15)):
            root.insert(random.randint(-10, 10))

print(f'\nThe full tree:')
root.print_tree()
print(f'\nRoot number is: {root.data}\n')
print(f'Height of tree: {root.tree_height()}')

mm, mx = root.min_max(root.data)
print()
print(f'min num is {mm}\n'
      f'max num is {mx}\n')

print(f'Reverced tree: ')
root.print_tree_rev()
