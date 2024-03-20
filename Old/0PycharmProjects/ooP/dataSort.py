from random import randint as r_num
# r_list = list(set([r_num(-10, 10) for i in range(r_num(3, 10))]))
# print(f'{r_list} - random list')
# r_list.sort()                       # sort only for list
# print(f'{r_list} - sorted list')
# print(f'{sorted(r_list)} - sorted list')


class Node:
    def __init__(self, _data):
        self.data = _data
# r_list.append(Node(r_num(0, 10)))
# r_list = [Node(r_num(-10, 10)) for i in range(5, 10)]


# def pred(val: Node):
#     return val.data


# for i in r_list:
#     print(i.data, end=' ')
# r_list.sort(key=lambda x: x.data)
# print()
# r_list.sort(key=pred)
# for i in r_list:
#     print(i.data, end=' ')
# r_list = sorted(r_list, key=pred)
# for i in r_list:
#     print(i.data, end=' ')

# r_list = [r_num(-10, 10) for i in range(10)]
# r_list.sort()
# print(f'{r_list} - random list\n')
def bin_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if target < arr[mid]:
            right = mid - 1
            continue
        if target > arr[mid]:
            left = mid + 1

    return -1
# print(bin_search(r_list, 3))


# size = 4
# data = [0]*size
# top = -1
#
#
# def push(x):
#     global top
#     if top >= size - 1:
#         print('Stack overflow exception')
#
#     else:
#         top += 1
#         data[top] = x
#
#
# def pop():
#     global top
#     if top == -1:
#         print('stack underflow exception')
#         return 'End!'
#     else:
#         top -= 1
#         return data[top+1]
#
#
# def peek():
#     global top
#     if top == -1:
#         print('stack is empty')
#         return 'End!'
#     else:
#         return data[top]
#
#
# push(1)
# push(2)
# push(3)
# push(4)

# print(pop())
# print(pop())
# print(pop())
# print(pop())

# print(peek())
# print(peek())
# print(peek())
# print(peek())

class MySteck:
    def __init__(self, size):
        self.size = size
        self.data = [0]*self.size
        self.top = -1

    def push(self, x):
        if self.top == (self.size - 1):
            print('full')
        else:
            self.top += 1
            self.data[self.top] = x

    def pop(self):
        if self.top == -1:
            print('empty')
        else:
            self.top -= 1
            return self.data[self.top + 1]


stack = MySteck(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

# rise exception ???
