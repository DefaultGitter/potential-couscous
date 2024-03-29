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
list_1 = [i for i in range(10)]
list_2 = (i for i in range(10))  # list comprehension
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