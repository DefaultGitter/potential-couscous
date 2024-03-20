"""
var = [i for i in range(10)]    # генерация списка
var2 = (i for i in range(10))    # генерация списка | list comprehension
print(var, '\n', type(var2))
"""
"""
match x:
    case "1":
        print("s")
    case 1:
        print("1")
    case 2:
        print("2")
    case _:
        print(f"{'3':%^10}")
"""
"""print(4, 5, "dsf", sep=" | ")
for i in range(8):
     print(i, end=" | ")"""
"""width = 4
for i in range(8):
    for h in range(width):
        for j in range(8):
            for w in range(width):
                if not (i+j) % 2:
                    print("#", end="  ")
                else:
                    print("-", end="  ")
        print()"""
"""var1 = ("word1", "word2", [1, 3])     # tuple
var1[2][0] = 42
var2 = tuple("word")                # w, o, r, d"""

l = [i for i in range(10)]
print(l)