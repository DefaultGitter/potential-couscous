def wordsInFile(_line: str, res: list, key=False):
    if key:
        res.append(_line)
        return res
    line_list = _line.split(' ')
    for _word in line_list:
        remove_it = set(_word).intersection({'.', ',', ':', ';', '!', '\n'})
        if remove_it:
            word_list = list(_word)
            for element in remove_it:
                word_list.remove(element)
            _word = ''.join(word_list)
        if _word:
            res.append(_word)
    return res


def moreThenSeven(words: list):
    res = []
    for _word in words:
        if len(_word) >= 7:
            res.append(_word)
    return f'\n'.join(res)


def findComma(_lines: tuple):
    _lines = list(_lines)
    for _line in _lines[::-1]:
        if ',' not in _line:
            i = _lines.index(_line)
            _lines.insert(i + 1, '************\n')
            break
    else:
        _lines.append('NO COMMA\n')
        _lines.append('************')
    return _lines


# task 1
with open('default.txt', 'r') as file:
    list_of_words = []
    for line_of_file in file:
        list_of_words = wordsInFile(line_of_file, list_of_words)

with open('MoreThenSeven.txt', 'w') as file:
    file.write(moreThenSeven(list_of_words))

# task 2
with open('default.txt', 'r') as file:
    list_of_lines = []
    for line_of_default in file:
        list_of_lines = wordsInFile(line_of_default, list_of_lines, True)
    list_of_lines = tuple(list_of_lines)

with open('default_copy.txt', 'w') as file:
    for line in list_of_lines:
        file.write(line)

# task 3
with open('default_copy_reversed.txt', 'w') as file:
    for line in list_of_lines[::-1]:
        file.write(line)

# task 4
with open('default_with_asterisk.txt', 'w') as file:
    lines = findComma(list_of_lines)
    for line in lines:
        file.write(line)

# task 5
with open('default.txt', 'r') as file:
    list_of_words = []
    for line in file:
        list_of_words = wordsInFile(line, list_of_words)
    first_letter = input(f'Enter a first letter of word: ')
    _count = 0
    for word in list_of_words:
        if first_letter.lower() == word[0].lower():
            _count += 1
    print(f'Num of words started by "{first_letter}" is {_count}')

# task 6
with open('default_with_asterisk.txt', 'r') as file:
    lines = []
    for line in file:
        lines = wordsInFile(line, lines, True)
    # print(lines)

with open('default_with_asterisk_changer.txt', 'w') as file:
    for line in lines:
        line_of_file = ''
        for letter in line:
            if letter == '*':
                letter = '&'
            elif letter == '&':
                letter = '*'
            line_of_file += letter
        file.write(line_of_file)
