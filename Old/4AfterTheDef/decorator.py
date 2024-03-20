def decor_f(inp_f):
    def output_f(v1):
        print('dc')
        v2 = v1[0::2]
        return inp_f(v2)

    return output_f


def decor_f2(inp_f):
    def output_f(*args):
        print(f'{" UP ":*^10}')
        inp_f(*args)
        print(f'{" DOWN ":*^10}')

    return output_f


@decor_f
def fu(_l: list):
    r = 0
    for i in _l:
        r += i
    return r


vv = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(fu(vv))

print(fu.__name__)
