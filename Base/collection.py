# Список можно вертеть как вздумается

list_1 = [i for i in range(10)]  # генерация списка
list_2 = (i for i in range(10))  # генерация списка | list comprehension

out = 1
if out:
    print(f'lis_1: {list_1}\n'
          f'{type(list_1)}\n')

    print(f'list_2: {list_2}\n'
          f'{type(list_2)}')

# Если присвоить список переменной,
# то в случае измения копии будет менятся и оригинал
# Для создания независимой копии
# С сохранением всех параметров и типов используется метод .copy()
l_cp = list_1.copy()
# Для клонирования с сохранением только содержимого можно использовать конструктор классов
l_copy = list(list_1)

l_copy.append('anything')
print(l_copy)

l_copy.reverse()
print(l_copy)

# l_copy['index']
print(f'Fourth element: {l_copy[4]}')
# l_copy['start', 'end', 'step']
print(f'List from second element to last, reversed: {l_copy[2::-1]}')
print(f'Every second: {', '.join(map(str, l_copy[::2])):>25}')
# Метод 'separator'.join(list) работает только на элементах типа str
# Для обьединения числовой коллекции нужно переформатировать элементы в строковый тип
# через функцию map(конструктор класса, список)

# var1 = ("word1", "word2", [1, 3])  # tuple
# var1[2][0] = 42

# var2 = tuple("word")  # w, o, r, d"""
