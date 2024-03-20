def words_in_file(line: str, res: list, key=False):
    if key:
        res.append(line)
        return res
    line_list = line.split(' ')
    for word in line_list:
        remove_it = set(word).intersection({'.', ',', ':', ';', '!', '\n'})
        if remove_it:
            word_list = list(word)
            for element in remove_it:
                word_list.remove(element)
            word = ''.join(word_list)
        if word:
            res.append(word)
    return res


def moreThenSeven(words: list):
    res = []
    for word in words:
        if len(word) >= 7:
            res.append(word)
    return f'\n'.join(res)


# task 1
with open('default.txt', 'r') as file:
    list_of_words = []
    for line_of_file in file:
        list_of_words = words_in_file(line_of_file, list_of_words)

with open('MoreThenSeven.txt', 'w') as file:
    file.write(moreThenSeven(list_of_words))


# task 2
with open('default.txt', 'r') as file:
    list_of_lines = []
    for line_of_default in file:
        list_of_lines = words_in_file(line_of_default, list_of_lines, True)

with open('default_copy.txt', 'w') as file:
    for line in list_of_lines:
        file.write(line)
