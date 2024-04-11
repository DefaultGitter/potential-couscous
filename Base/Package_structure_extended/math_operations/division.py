__all__ = ['div']


def div(x: int, y: int):
    if (x == 0) or (y == 0):
        exit("Division by zero!!!")
    else:
        return x / y
