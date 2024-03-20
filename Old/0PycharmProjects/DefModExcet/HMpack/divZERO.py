import HMpack


def div(x: str, y: str):
    try:
        return HMpack.construct(x) / HMpack.construct(y)
    except ZeroDivisionError:
        return 'You`ve tried to destroy the WHOLE UNIVERSE!!!'


if __name__ == '__main__':

    # no func method

    digit = input('Enter first number: '), input('Enter second number: ')
    try:
        print(f'The result of division is: {HMpack.construct(digit[0]) / HMpack.construct(digit[1])}')
        pass
    except ZeroDivisionError as mess:
        print(mess)
    except TypeError as mess:
        print(mess)
