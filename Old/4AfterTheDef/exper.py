import time


def timing(fn):
    def out(x, y, z):
        start = time.time()
        return fn(x, y, z), start

    return out


def logged(fn):
    def out(x, y, z):
        print('\ndc')
        print(f'func name: {fn.__name__}')
        print(f'func arguments: {x}, {y}, {z}')
        return fn(x, y, z)

    return out


@logged
def run(v1, v2, v3):
    print('function works')


# @logged
@timing
def walk(v1, v2, v3):
    time.sleep(2)
    return 'function lives'


# run(3, 2, 1)
x, y = walk('arg1', 'arg2', 'arg3')
end = time.time()
print(f'Func result: {x}\n'
      f'Program time: {end - y}')
