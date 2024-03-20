from zipfile import ZipFile, ZIP_DEFLATED

# v1 = ZipFile('test.zip', 'w')
# v1.close()

# with ZipFile('test.zip', 'w', compression=ZIP_DEFLATED, compresslevel=3) as myZip:
#     myZip.write('test.txt', 'ttt.txt')
#     myZip.write('test.txt', 'tt.txt')
#     myZip.write('test.txt', 't.txt')

# with ZipFile('test.zip', 'r') as myZip:
#     for i in myZip.infolist():
#         print(i.filename)
#     for i in myZip.namelist():
#         print(i)
#     for i in myZip.infolist():
#         if i.is_dir():
#             print(f'dir {i.filename}')
#         else:
#             print(f'file {i.filename}')
#     res = myZip.getinfo('ttt.txt')
#     print(res.filename)
#     myZip.extractall(members=['t.txt', 'ttt.txt'])
#     myZip.extract('t.txt')
#     v = myZip.read('ttt.txt')
#     print(type(v))
#     print(v.decode())
#     with myZip.open('tt.txt', 'r') as file:
#         r = file.read()
#         print(r.decode('utf-8'))
