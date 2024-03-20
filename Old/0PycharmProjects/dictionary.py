#   Словарь / dictionary
#   Хранит ключ и значение

# var1 = {1: "here", 2: "we"}
# var2 = {3: "go"}
# # var1 = {1: "here", 2: "we", 3: "go"}  # {key: value}
# var1[4] = "again"
# for i in var1:
#     print(i)
#     print(var1[i])

# for i in var1.values():
#     print(i)

# for i in var1.items():
#     print(i)

# for x, y in var1.items():
#     print(x, y)

# print(var1.items())

# for x in var1.keys():
#     print(x)
# print(var1.keys())

# var2 = {}
# var2 = dict()

# var1.get(0)
# print(var1.get(0))
# print(var1.get(20, "Oh shit"))

# del var1[2]
# print(var1)

# print(var1.pop(2, "press f"))
# print(var1.pop(20, "press f"))
# print(var1)

# var1.clear()

# test = var1.copy()

# var1.update(var2)
# print(var1)

# users = {
#     "Key1": {  # value1
#         "subkey1": "value1",
#         "subkey2": "value2"
#     },
#     "Key2": {  # value2
#         "subkey1": "value1",
#         "subkey2": "value2",
#         "subkey3": "value3"
#     }
# }
# users["Key1"]["subkey1"] = "123456789963852741"
# print(users["Key1"]["subkey1"])
# print(users.get("Key1").get("subkey1"))

dict1 = {}

dict1["колір"] = "color"
dict1["банан"] = "banana"
dict1["лук"] = ["bow", "onion"]

choice = None

while choice != "":
    choice = input(f"{' Input num of func from 0 to 3 ':^50}\n")
    if choice.isnumeric():
        choice = int(choice)
    match choice:
        case 0:
            add_word = input(f"Do you wanna add new WORD or TRANSLATE?\n")
            match add_word.upper():
                case "WORD":
                    add_word = tuple(input(f'input word and translate separated by "-"\n').split("-"))
                    dict1[add_word[0]] = add_word[1]
                case "TRANSLATE":
                    add_word = input(f"Enter word")
                    dict1[add_word].append(input(f"Enter new translate"))
        case 1:
            rem_word = input(f"delete WORD or TRANSLATE")
            match rem_word.upper():
                case "WORD":
                    rem_word = input(f"enter word for remove\n").lower()
                    dict1.pop(rem_word, "there is no word")
                case "TRANSLATE":
                    rem_word = input(f"enter word\n")
                    if type(dict1[rem_word]) == type(tuple()):
                        dict1[rem_word].pop(dict1[rem_word].index(input(f"enter translate")))
                    else:
                        print(f"This word has only one translate - \'{dict1[rem_word]}\'")
                        print(f"Translate was deleted")
                        dict1[rem_word] = "-"
        case 2:
            find_word = input(f"enter word, which you wanna translate")
            print(dict1[find_word])
        case 3:
            change_word = input(f"enter word")
            if type(dict1[change_word]) == type(list()):
                print(dict1[change_word])
                change_word1 = input(f"which translate do you wanna change?\n")
                dict1[change_word][dict1[change_word].index(change_word1)] = input(f"enter new translate")
            else:
                change_word1 = input(f"enter new translate?\n")
                dict1[change_word] = change_word1

print(dict1)
