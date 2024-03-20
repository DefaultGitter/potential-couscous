# Користувач вводить з клавіатури набір чисел. Отримані числа необхідно зберегти до списку.
# Після чого потрібно показати меню, в якому запропонувати користувачеві набір пунктів:
# 1. Додати нове число до списку
# (якщо таке число існує у списку, потрібно вивести повідомлення користувачу про це без додавання числа).
# 2. Видалити всі входи числа зі списку (користувач вводить з клавіатури число для видалення).
# 3. Показати вміст списку (список потрібно показати спочатку).
# 4. Перевірити чи є значення у списку.
# 5. Замінити значення у списку (користувач визначає чи замінити тільки перше входження або всі входження).
# Залежно від вибору користувача виконується дія, після чого меню з'являється знову.
import random


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class DefC:
    def __init__(self):
        self.head = None
        self.tail = None

    def ex_add(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def changer(self, data, new_data, _key):
        current = self.head
        while current:
            if current.data == data:
                current.data = new_data
                if 'all' not in key.lower():
                    break
            current = current.next

    def founder(self, element):
        current = self.head
        while current:
            if current.data == element:
                return True
            current = current.next

    def printer(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            # print(current)
            current = current.next

    def remover(self, element):
        current = self.head
        end = self.tail
        while current:
            self.tail = current
            if self.head.data == element:
                # print('Head')
                self.head = current.next
            if current == end:
                break
            if current.next == end:
                if current.next.data == element:
                    # print('Tail')
                    end = current
                    current.next = None
            if current.next.data == element:
                # print('Body')
                # print(self.tail)
                self.tail.next = current.next.next
            current = current.next
        self.tail = end


ll = DefC()
for i in range(5):
    ll.ex_add(random.randint(0, 10))
ll.printer()
while True:
    print('''
    0 - exit
    1 - add element
    2 - delete element
    3 - show the list
    4 - is it in list
    5 - change element
    ''')
    choice = input(f'Enter a num of func: ')
    match choice:
        case '0':
            break

        case '1':
            el = int(input(f'Enter a number: '))
            if ll.founder(el):
                print(f'This list already has {el}')
            else:
                ll.ex_add(el)

        case '2':
            el = int(input(f'Enter an element to delete: '))
            ll.remover(el)
            print(f'Removal successful!')

        case '3':
            ll.printer()

        case '4':
            el = int(input('Enter a num to find: '))
            if ll.founder(el):
                print(f'{el} in list')
            else:
                print(f'This list has no {el}')

        case '5':
            el = int(input(f'Enter an element to change: '))
            key = input(f'Change only FIRST match or ALL matches of this element? ')
            new_el = int(input(f'Enter e new number: '))
            ll.changer(el, new_el, key)
            print(f'Change successful!')
