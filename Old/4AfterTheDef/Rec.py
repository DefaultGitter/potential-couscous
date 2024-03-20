# _x = lambda x, y: (
#     x + y,
#     x - y
# )
# print(_x(3, 8))
# print(type(_x(3, 8)))


def fn(lst, alg=None):
    if alg is None:
        return lst
    else:
        res = []
        for i in lst:
            if alg(i):
                res.append(i)
        return res


def alg1(x):
    if not x % 2:
        return True
    else:
        return False


# ls1 = [1, 3, 4, 6, 9, 7, 5]
# # print(fn(ls1, alg1))
# print(fn(ls1, lambda x: not x % 2))


