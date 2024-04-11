import package


def div(x: str, y: str):
    try:
        return package.construct(x) / package.construct(y)
    except ZeroDivisionError:
        return 'You`ve tried to destroy the WHOLE UNIVERSE!!!'


if __name__ == '__main__':

    # no func method

    digit = input('Enter first number: '), input('Enter second number: ')
    try:
        print(f'The result of division is: {package.construct(digit[0]) / package.construct(digit[1])}')
        pass
    except ZeroDivisionError as mess:
        print(mess)
    except TypeError as mess:
        print(mess)
