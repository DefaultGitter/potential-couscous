import calc


#
def main():
    print(f'Example: (2+3)*8+(13+(9*2))'
          f'\nEnter a formula as an example:')
    print(f'Result: {calc.calculator(input())}')


if __name__ == '__main__':
    main()
