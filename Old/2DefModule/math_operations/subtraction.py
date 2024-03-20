__all__ = ['sub']


def sub(value: list):
    res = 0
    for i in value:
        res -= i
    return res
