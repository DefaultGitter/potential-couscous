def sum_of_numbers(list_of_numbers):
    res = 0
    for i in list_of_numbers:
        res += i
    return res


def min_of_numbers(list_of_numbers):
    min_of_num = list_of_numbers[0]
    for i in list_of_numbers:
        if i < min_of_num:
            min_of_num = i

    return min_of_num


def prime_numbers(list_of_numbers):
    num_of_prime = 0
    for number in list_of_numbers:
        for i in range(2, number + 1):
            if number == i:
                num_of_prime += 1
            elif number % i == 0:
                break

    return num_of_prime


def delete_num(list_of_numbers, _delete):
    _count = 0
    for i in list_of_numbers:
        if _delete == i:
            list_of_numbers.pop(list_of_numbers.index(i))
            _count += 1
    return f"Количество удалённых элементов: {_count}"


def list_plus_list(list1, list2):
    list3 = list(list1)
    for i in range(len(list2)):
        list3.append(list2[i])
    return list3


def power(list_of_numbers, poow):
    result_list = []
    for i in range(len(list_of_numbers)):
        result_list.append(list_of_numbers[i] ** poow)
    return result_list


def clear_list(ex):
    ex = ex.split(",")
    for i in range(len(ex)):
        ex[i] = ex[i].strip()
        if ex[i].isnumeric():
            ex[i] = int(ex[i])
    return ex


ex_list = input(f"Enter your list of numbers separated by coma\n")
ex_list = clear_list(ex_list)
_def = int(input(f"Enter the number of function from 1 to 6: "))
match _def:
    case 1:
        print(f"Sum of numbers is: {sum_of_numbers(ex_list)}")
    case 2:
        print(f"Min number is: {min_of_numbers(ex_list)}")
    case 3:
        print(f"Prime numbers in your list is: {prime_numbers(ex_list)}")
    case 4:
        _del = int(input("Which number you wanna delete? "))
        print(f"Number of deleted elements is {delete_num(ex_list, _del)}")
    case 5:
        sec_list = input("Enter your second list the same way")
        sec_list = clear_list(sec_list)
        print(f"{list_plus_list(ex_list, sec_list)}")
    case 6:
        POW = int(input(f"Enter the power"))
        print(power(ex_list, POW))
