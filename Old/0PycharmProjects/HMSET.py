def sep_word(_line: str):
    _line = _line.split(",")
    for _i in _line:
        _line[_line.index(_i)] = _i.strip().capitalize()
    return _line


countries = {"Canada", "China", "United States", "Brazil", "Australia", "India", "Argentina", "Kazakhstan", "Algeria",
             "DR Congo", "Greenland", "Saudi Arabia", "Mexico"}
fl = f"{'#':#^50}"
print(f"{fl}\n{' Country list ':#^50}\n{fl}")

countries_copy = list(countries)
mtl = []
i, start = 0, 0
while i < len(countries_copy):
    mtl.append(countries_copy[i])
    if len(" | ".join(mtl[start:i])) >= 50:
        mtl.pop(i)
        i -= 1
        line = " " + " | ".join(mtl[start:i]) + " "
        print(f"{line:#^50}")
        start = i
    elif i == len(countries_copy) - 1:
        line = " " + " | ".join(mtl[start:]) + " "
        if len(line) >= 50:
            line = " " + " | ".join(mtl[start:i]) + " "
            print(f"{line:#^50}")
            line = " " + " | ".join(countries_copy[i:]) + " "
            print(f"{line:#^50}")
        else:
            print(f"{line:#^50}")
    i += 1
print(
    f"{fl}\n{' This program can do 4 things with set ':#^50}\n{'ADD element:':<49}1\n{'REMOVE element:':<49}2\n"
    f"{'FIND the element with yours letters:':<49}3\n{'Tell you if your countries are IN the list:':<49}4")
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
