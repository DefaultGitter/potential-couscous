def fn_format(text: str):
    end = None
    for i in range(len(text)):
        if (i < len(text) - 2) and ("..." in text[i:i - 3:-1]):
            print(f"{text[0:i + 1]}")
        elif (i > 1) and (text[i] == "\""):
            print(f"{text[text.find('...') + 3:i + 1]:>52}")
            end = i
        elif (i > 1) and end:
            print(f"{text[end + 1:]:>52}")
            break


def fn_div2(var: list):
    start = min(var)
    end = max(var)
    res = []
    for i in range(start + 1, end):
        if i % 2 == 0:
            res.append(i)
    return res


def fn_square(symbol: str, length: int, key: bool):
    for y in range(length):
        for x in range(length):
            if length - 1 > y > 0:
                if length - 1 > x > 0:
                    if key:
                        print(symbol, end=" ")
                    else:
                        print(" " * len(symbol), end=" ")
                else:
                    print(symbol, end=" ")
            else:
                print(symbol, end=" ")
        print()


def fn_digits(num: list): return list(map(len, map(str, num)))


def main():
    choice = (input(f"Enter a num of function: 1, 2, 3 or 6\n"))
    if choice.isdigit():
        choice = int(choice)
    match choice:
        case 1:
            fn_format("\"Don`t compare yourself with anyone in this world..."
                      "if you do so, you are insulting yourself.\"Bill Gates")

        case 2:
            print(
                f'Even numbers between yours are: '
                f'{", ".join(map(str, fn_div2(list(map(int, input(f"Enter you numbers sep by comma: ").split(","))))))}'
            )
            # I`m sorry for this line... It was an experiment
            # And IT`S A LIVE!!! I mean it works...

        case 3:
            length = int(input(f"Enter square side length: "))
            symbol = input(f"Enter any symbol: ")
            key = input(f"Square might be EMPTY or FULL? ")
            match key.lower():
                case "empty":
                    key = False
                case "full":
                    key = True
            fn_square(length=length, symbol=symbol, key=key)

        case 6:
            num = input(f"Enter your numbers separated by comma: ").split(",")
            print(f'Length of your numbers are: {fn_digits(list(map(int, num)))}')

        case "exit":
            exit(code="Program finished")
        
    main()


main()
