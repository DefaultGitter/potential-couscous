import math_operations


def link(symbol: str):
    match symbol:
        case '+':
            return math_operations.add
        case '-':
            return math_operations.sub
        case '*':
            return math_operations.multi
        case '/':
            return math_operations.div


def idc(x, y, _link):
    return _link(x, y)


def spell(_data: list):
    while len(_data) > 1:
        for i in range(len(_data)):
            if str(_data[i]) in '*/':
                ind_i = _data.index(_data[i])
                _data[ind_i] = idc(_data[ind_i - 1], _data[ind_i + 1], link(_data[i]))
                _data.pop(ind_i + 1)
                _data.pop(ind_i - 1)
                break

        for i in range(len(_data)):
            if str(_data[i]) in '+-':
                ind_i = _data.index(_data[i])
                _data[ind_i] = idc(_data[ind_i - 1], _data[ind_i + 1], link(_data[i]))
                _data.pop(ind_i + 1)
                _data.pop(ind_i - 1)
                break
    else:
        return _data[0]


def dark_magick(_data: list):
    for i in _data:
        if type(i) == list:
            _data[_data.index(i)] = dark_magick(i)
    else:
        return spell(_data)


def calculator(data: str):
    data = math_operations.rewrite(data)
    return dark_magick(data)

