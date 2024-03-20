# in > str
# separate words and find a number of words
def sep_words(word_list):
    word_list = word_list.split(",")
    i = 0
    len_of_list = len(word_list) - 1
    while i <= len_of_list:
        if "." in word_list[i]:
            sub_word = word_list[i].split(".")
            for j in sub_word:
                if j and j != " ":
                    word_list.insert(i, j.strip())
                    len_of_list += 1
                    i += 1
            word_list.pop(i)
        else:
            word_list[i] = word_list[i].strip()
        i += 1
    return tuple(word_list)


word = input(
    f"{' Enter your fruits separated by comma or period ':#^70}\n%s" % f"{'List of fruits:'}"
)
find_word = input(f"{'Enter, what do you wanna find in your list:'}")

word = sep_words(word)
find_word = sep_words(find_word)

num_of_founded = []
_count = 0
for i in find_word:
    for j in word:
        if i.upper() in j.upper():
            _count += 1
    num_of_founded.append(_count)
    _count = 0

while _count <= len(find_word) - 1:
    print(f"{find_word[_count]} - {num_of_founded[_count]}")
    _count += 1

car_list = ("car1", "car2", "car3", "car1")
find_word = ("car1")
