import os
import stat

# os.mkdir(r'C:\test')
# os.mkdir('test')
# os.rmdir('test')
# os.rename('test', 'test.txt')
# os.rename('ttt.txt', 'ff.txt')
# os.remove('ff.txt')

# print(os.path.exists('test.txt'))

# print(os.path.abspath('test.txt'))

# print(os.path.dirname(r'test\text.txt'))

# print(os.path.isdir('test'))
# print(os.path.isfile(r'test\text.txt'))
# os.mkdir(r'test2\test3')

# os.chdir('test')
# os.mkdir(r'test4')

# print(os.listdir('test'))

# print(os.curdir)
# print(os.path.abspath('..'))
# print(os.path.abspath(os.curdir))


# p1 = os.path.abspath(os.curdir)
# print(p1)
# p2 = os.path.abspath('..')
# print(p2)
# os.chdir(p2)
# print(os.path.abspath('..'))

# print(os.path.abspath(__file__))

# print(os.getcwd())

# for i in os.scandir(os.curdir):
# for i in os.scandir(os.getcwd()):
#     print(i.name)

# print(os.access(r'test\text.txt', os.F_OK))
# print(os.access(r'test\text.txt', os.R_OK))
# print(os.access(r'test\text.txt', os.W_OK))

# os.chmod(r'test\text.txt', stat.S_IWUSR)
# os.chmod(r'test\text.txt', stat.S_IRUSR)
# os.chmod(r'test\text.txt', stat.S_IRWXU)
# os.chmod(r'test\text.txt', 0o600)       # oct system owner/group/public to rwx
