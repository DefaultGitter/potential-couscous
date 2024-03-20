def remover(lst: list, element):
    if element not in lst:
        return lst
    el = lst.pop(lst.index(element))
    return remover(lst, el)


l_test = [1, 2, 3, 2, 4, 5, 1, 2]
print(f'Original list: \n{l_test}\n\nThis list without "2": \n{remover(l_test, 2)}')
