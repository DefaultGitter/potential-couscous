def main():
    n = 0

    def it():
        nonlocal n
        n += 1
        print(n)

    return it
# f = main()
# f()
# f()


def mm(x):
    def nn(y):
        return x + y

    return nn


f = mm(5)
print(f(3))
