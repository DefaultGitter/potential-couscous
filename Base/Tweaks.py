# e.t.c.
"""
# del method can delete a particular element
del list_name
del list[index]
del dict[key]

"""

# output
"""
print(1, 2, 3, sep=' | ')       # separation
for i in range(8):
    print(i, end=" | ")         # out without \n

print(f"{' 3 ':%^10}")          # Format center
print(f"{' 3 ':%<10}")          # Format left
print(f"{' 3 ':%>10}")          # Format right
"""

# collections
"""
# list
list_1 = [i for i in range(10)]
list_2 = (i for i in range(10))  # list comprehension

list_1.extend('asd')        # unpack collection ('a','s','d') into list_1

list_1.pop(index)
list_1.remove(value)

list_1.index(value, start_index, end_index)     # start/end optional

# dict
dict_1 = {1: 'Value1', 2: 'Value2', 3: 'Value3'}

for i in dict_1.values():
    print(i)

for x in dict_1.keys():
    print(x)

for x, y in dict_1.items():
    print(x, y)

print(dict_1.get(1))                  # return Value1
print(dict_1.get(20, "Oh shit"))      # return 'Oh shit', because dict has no key 20

print(dict_1.pop(0, 'Have not this key'))                 # return message
print(dict_1.pop(1, 'Element by key 1 was removed'))      # return Value1

dict_1.clear()

dict_2 = {4: 'Value4', 5: 'Value5'}
dict_1.update(dict_2)           # unpack dict_2 into dict_1
"""

# definition
"""
def def1(v1, v2):
    return

def1(0, 1)

def def2(*, v1, v2):            # name control after *
    return

def2(v1=0, v2=1)

def def3(v1, v2, /, v3, v4):    # queue control before /
    return

def3(0, 1, 2, v4=4, v3=3)
"""

# decorator
"""
def decor(fn):
    def out(var1, var2):
        # some code
        return fn(var1, var2)
        
    return out


@decor
def func_under_decor(var1, var2):
    # some code
    return var1, var2

"""

# *args, **kwargs
"""
a1 = [1, 2, 3, 4]
a2 = [*a1, 5, 6, 7]             # a1 has been unpacked in a2

def def1(*var):
    for i in var:  # var is list
        print(i)


def1(2, 4, 6, 9)


# **kwargs has name and return dictionary
def def2(**var):
    for name, num in var.items():
        print(f'{name} - {num}')


def2(a=2, s=4, d=6, f=9)
"""