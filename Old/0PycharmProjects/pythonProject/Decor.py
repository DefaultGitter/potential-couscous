def validate(fn):
    def out(x, y):
        try:
            return fn(int(x), int(y))
        except ZeroDivisionError:
            return 'You`ve tried to destroy the whole universe!!!'
        except ValueError:
            return 'Wrong data'

    return out


@validate
def div(x: int, y: int):
    return x / y


value = ['t', 0, '3']

for i in value:
    r = div(3, i)
    print(f'Result of division: {r}')
    
    if type(r) in (int, float):
        print('\nYou can continue your code')
        break

input()
