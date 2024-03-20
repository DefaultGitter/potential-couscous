# Список можно вертеть как вздумается

list_1 = [i for i in range(10)]  # генерация списка
list_2 = (i for i in range(10))  # генерация списка | list comprehension

print(f'list_1: {list_1}\n'
      f'{type(list_1)}\n')

print(f'list_2: {list_2}\n'
      f'{type(list_2)}')

# var1 = ("word1", "word2", [1, 3])  # tuple
# var1[2][0] = 42

# var2 = tuple("word")  # w, o, r, d"""
