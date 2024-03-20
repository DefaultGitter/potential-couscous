s = 'STR'
# s = input('FFF: ')
# n = int(s)

try:
    n = int('1f')
# except ValueError:
#     raise TypeError('fuck')
except ValueError as mess:
    print(mess)
# except TypeError as mess:
#     print(mess)
else:
    print('ffff')
# finally:            # всегда срабатывает
#     print('fin')

# try:
#     print(n)
# except NameError:
#     print('No n')
