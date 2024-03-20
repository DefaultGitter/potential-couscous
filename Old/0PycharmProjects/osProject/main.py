import os


def cleaner(f_path, item_list):
    os.chdir(f_path)
    for item in item_list:
        if os.path.isfile(item):
            os.remove(item)
        elif os.path.isdir(item):
            collection = os.listdir(item)
            if not collection:
                os.rmdir(item)
            else:
                cleaner(item, collection)
                os.chdir('..')
                os.rmdir(item)


# task 1

# way = input('Enter a path to your folder: ')
# package = os.listdir(way)
# print(package)

# task 2
# remove_item = input('Enter a name of file or folder to delete: ')
# cleaner(way, [remove_item])

# task 3
def FileManager(f_path):
    print(os.path.abspath('.'))
    print(os.listdir(f_path))
    print('''
    1 - remove item
    2 - rename item
    3 - change directory
    4 - step back
    0 - finish program
    ''')
    choice = input('Enter a num of function: ')
    match choice:
        case '1':
            rem_item = input('Enter a name of file or folder to delete: ')
            cleaner(way, [rem_item])
        case '2':
            item = input('Enter a name of item to rename: ')
            new_name = input('Enter e new name: ')
            os.rename(item, new_name)
        case '3':
            new_way = input('Enter a path to new directory: ')
            os.chdir(new_way)
        case '4':
            os.chdir('..')
        case '0':
            return True


way = input('Enter a path to your folder: ')
while True:
    if FileManager(way):
        break
