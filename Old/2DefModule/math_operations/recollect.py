__all__ = ['re']


def re(data: str):
    def sep(sub_data: str):
        for symbol in sub_data:
            if symbol == '(':
                _element = ''
                brackets_count = 0
                brackets_limit = sub_data.count('(', 0, sub_data.index(')'))
                for _symbol in sub_data:
                    if brackets_count == brackets_limit:
                        break
                    else:
                        if _symbol == ')':
                            brackets_count += 1
                        _element += _symbol
                _element = ''.join(list(_element))
                return _element

    i = 0
    f = []
    while i < len(data):
        # print(data[i], end=' ')
        print(f'Iter {i}')
        element = sep(data[i:])
        if element:
            print(f'Len of res {len(element)}')
            i += len(element)
            f.append([element])
        i += 1
    print(f)


important_sep = ('()', '*/', '+-')
if __name__ == '__main__':
    print('\n', re(data='(12+(34+56))+7'))
