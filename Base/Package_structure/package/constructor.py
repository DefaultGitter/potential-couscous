def construct(data: str):
    try:
        return int(data)
    except ValueError as _mess:
        exit('Wrong data')


if __name__ == '__main__':

    # no func method

    digit = input('Enter something: ')
    try:
        int(digit)
        print('It`s a num!!!')
    except ValueError:
        print('It`s not a num :-(')
