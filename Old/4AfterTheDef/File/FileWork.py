# try:
#     file = open('mmm.txt', 'w')
#     s = ['he-he-he', '#', 'fucker']
#     # file.writelines(s])
#     file.write(s[0])
#     file.write('\nntai')
# except Exception as ex:
#     print(ex)
# finally:
#     file.close()

# with open('mmm.txt', 'w') as fil:
#     fil.write('hi-hi-hi')
#     print('Some text', file=fil)

# with open('mmm.txt', 'r') as fil:
# for i in fil:
#     print(i)
# r = ' '
# while r:
#     r = fil.readline()
#     print(r)
#     print(fil.readline())
#     print(fil.readline())
#     print(fil.readline())
#     print(fil.readline())
#     print(fil.read())
#     r = fil.readlines()
#     print(r)
#     fil.seek(5)
#     print(fil.read())
#     fil.seek(5, 0)
#     print(fil.read())
#     fil.seek(5, 1)
#     print(fil.read())
#     fil.seek(5)
#     print(fil.read())

# with open('mmm.txt', 'wb') as file:
#     r = str.encode('words')
#     print(r)
#     print(type(r))
#     file.write(r)
#
# with open('mmm.txt', 'rb') as file:
#     # file.seek(-2, 2)
#     # print(file.read())
#     file.seek(2, 1)
#     print(file.read())


# import pickle
# str1 = 'symbols'
# var1 = '123'
# with open('test.bin', 'wb') as file:
#     # pickle.dump('sss', file)
#     # pickle.dump(str1, file)
#     # pickle.dump(var1, file)
#     pickle.dump([['as', 1], ['ds', 2], ['fd', 3]], file)
#
# with open('test.bin', 'rb') as file:
#     res1 = pickle.load(file)
#     # res2 = pickle.load(file)
#
#     print(res1)
#     # print(res2)


import shelve

# with shelve.open('test2') as file:
#     file['key1'] = 'val1'
#     file['key3'] = 'val3'
#     file['key2'] = 'val2'

with shelve.open('test2') as file:
    # del file['key3']
    # file.pop('key3', 'def')
    # file['key3'] = 'y'
    file['key5'] = [1, 'ss', int]

with shelve.open('test2') as file:
    # print(file['key2'])
    # print(file['key1'])
    # print(file.get('key4', 'def'))
    for i in file.items():
        print(i)
