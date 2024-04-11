def brackets(_data: list, num_brackets: int):  # преобразование содержимого скобок в список
    sub_data = _data.copy()
    start = 0
    end = len(_data) - 1
    for i in range(len(_data)):
        if _data[i] == '(':
            num_brackets += 1
            j = i
            while _data[j] != ')':
                j += 1
                if _data[j] == '(':
                    # i = j
                    break
            else:
                end = j
                start = i + 1
                break
    for i in range(len(_data[start:end])):
        sub_data.pop(start)
    return sub_data, num_brackets, _data[start:end]


def find_brackets(_data: list):  # поиск скобок в списке, отправка содержимого на преобразователь
    sub_data = _data.copy()
    num_brackets = 0
    while '(' in sub_data:
        sub_data, num_brackets, part = brackets(sub_data, num_brackets)
        c = 0
        for i in range(len(sub_data)):
            if sub_data[i] == '(':
                c += 1
            if c == num_brackets:
                sub_data.pop(i)
                sub_data[i] = part
                num_brackets = 0
                break
    return sub_data


def rewrite(_data: str):  # преобразование в подходящий список
    res = []
    i = 0
    while i < len(_data):
        if _data[i] in '()*/+-':
            res.append(_data[i])
            i += 1
        elif _data[i].isnumeric():
            for j in range(len(_data[i:])):
                if (not _data[i:][j].isnumeric()) or (i == len(_data) - 1):
                    if i == len(_data) - 1:
                        res.append(int(_data[i:]))
                        i += len(_data[i:])
                    else:
                        res.append(int(_data[i:i + j]))
                        i += len(_data[i:i + j])
                    break
        elif _data[i] == ' ':
            i += 1
    return find_brackets(res)
