# in > str
# separate words and find a number of words
def sep_words(word_list):
    word_list = word_list.split(",")
    i_def = 0
    len_of_list = len(word_list) - 1
    while i_def <= len_of_list:
        if "." in word_list[i_def]:
            sub_word = word_list[i_def].split(".")
            for j_def in sub_word:
                if j_def and j_def != " ":
                    word_list.insert(i_def, j_def.strip())
                    len_of_list += 1
                    i_def += 1
            word_list.pop(i_def)
        else:
            word_list[i_def] = word_list[i_def].strip()
        i_def += 1
    return tuple(word_list)


word = input(
    f"{' Enter your fruits separated by comma or period ':#^70}\n%s" % f"{'List of fruits:'}"
)
word = sep_words(word)
print(f"You`ve enter {len(word)} fruits")
find_word = input(f"{'Enter, what do you wanna find in your list:'}")

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

car_manufacturer_list = ("Toyota", "Volkswagen Group", "Hyundai", "General Motors", "Ford",
                         "Nissan", "Honda", "Fiat Chrysler", "Renault", "Groupe PSA",
                         "Suzuki", "SAIC", "Daimler", "Toyota")

print(f"{'We have a list of car manufacturers':*^30}\n{' | '.join(car_manufacturer_list)}")
find_word = []
i = 0
print("Enter manufacturer and word to replace separated by \"-\" like as in the example:\n"
      "Nissan - Oniichan")
while True:
    find_word.append(input())
    if find_word[i] == "":
        find_word.pop(i)
        break
    find_word[i] = find_word[i].split("-")
    i += 1

car_manufacturer_list = list(car_manufacturer_list)
for i in range(len(find_word)):
    for j in range(len(car_manufacturer_list)):
        if find_word[i][0].strip() == car_manufacturer_list[j]:
            car_manufacturer_list[j] = find_word[i][1].strip()
car_manufacturer_list = tuple(car_manufacturer_list)
print(car_manufacturer_list)

list_of_numbers = input("Enter a list of numbers separated by comma:")
list_of_numbers = tuple(sep_words(list_of_numbers))
count_list = []
for i in list_of_numbers:
    count_list.append(len(i))
count_list.sort()
# print(count_list)
num_of_founded = []
founded_num = []
_count = 1
i = 0
copy_num = None
while i < len(count_list):
    if not copy_num:
        if i == len(count_list) - 1:
            founded_num.append(count_list[i])
            num_of_founded.append(_count)
            break
        copy_num = count_list[i]
    elif copy_num == count_list[i]:
        _count += 1
    elif (copy_num != count_list[i]) and (i > 0):
        i -= 1
        founded_num.append(count_list[i])
        num_of_founded.append(_count)
        copy_num = None
        _count = 1
    i += 1

for i in range(len(founded_num)):
    print(f"{founded_num[i]} digits appear {num_of_founded[i]} times in one number ")
input()
