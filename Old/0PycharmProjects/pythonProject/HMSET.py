def sep_word(line: str):
    line = line.split(",")
    for _i in line:
        line[line.index(_i)] = _i.strip().capitalize()
    return line


countries = {"Canada", "China", "United States", "Brazil", "Australia", "India", "Argentina", "Kazakhstan", "Algeria",
             "DR Congo", "Greenland", "Saudi Arabia", "Mexico"}
fl = f"{'#':#^50}"
print(f"{fl}\n{' Country list ':#^50}\n{fl}")
len_of_line = 0
mtl = []
countries_copy = list(countries)
for i in range(len(countries_copy)):
    if len(mtl) >= 50:
        mtl = []

    mtl.append(countries_copy[i])
choice = input(f"{fl}\n{' What do you wanna do with this list? ':#^50}\n{fl}\n")
choice_list = ("1 add", "2 remove", "3 find", "4 in")
if choice in choice_list[0]:
    c_list = input(f"{' Enter countries separated by comma ':#^50}\n")
    c_list = list(sep_word(c_list))
    for i in c_list:
        countries.add(i)
elif choice in choice_list[1]:
    c_list = input(f"{' Enter countries separated by comma ':#^50}\n")
    c_list = list(sep_word(c_list))
    for i in c_list:
        countries.discard(i)
        if i not in countries:
            print(f"{f' List has no %s{i}%s ':#^50}" % ("\"", "\""))
elif choice in choice_list[2]:
    c_list = input(f"{' Enter letters without any separator ':#^50}\n")
    c_list = set(list(c_list.upper()))
    _countries = []
    for i in countries:
        if set(i.upper()).issuperset(c_list):
            _countries.append(i)
    if _countries:
        print(f"These countries has your letters:\n{' | '.join(_countries)}")
    else:
        print(f"{' There are on countries with all yours letter ':#^50}")
elif choice in choice_list[3]:
    c_list = input(f"{' Enter countries separated by comma ':#^50}\n")
    c_list = set(sep_word(c_list))
    for i in c_list:
        if {i}.intersection(countries):
            print(f"{i} in the list")
        else:
            print(f"There are no {i} in the list")
