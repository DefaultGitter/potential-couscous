'''
создать объект      +
сохранить в json    +
заархивировать      +
достать из архива   +
'''

from zipfile import ZipFile, ZIP_DEFLATED
import json

Book_dict = {
    "F. Scott Fitzgerald": {
        "The Great Gatsby": {
            "genre": "Tragedy",
            "year of publication": "April 10, 1925",
            "number of pages": "208 pages",
            "publisher": "Charles Scribner's Sons"}}}

with open('my_secret_data.json', 'w') as file:
    json.dump(Book_dict, file)

with ZipFile('secret_archive.zip', 'w', compression=ZIP_DEFLATED, compresslevel=3) as NotArchive:
    NotArchive.write('my_secret_data.json', 'top_secret.json')
    archive_name = NotArchive.filename

key = input('Do you want to extract file from archive?\nY/N ')
if key.upper() in ['Y', 'YES']:
    name = input(f'Enter a name of archive: ').strip()
    if '.zip' not in name:
        name += '.zip'
else:
    exit('The end!')

try:
    with ZipFile(name, 'r') as maybeZip:
        print('This archive has these files:')
        for i in maybeZip.namelist():
            print(i)
        file_name = input('Enter a name of file, to extract: ')
        try:
            maybeZip.extract(file_name)
        except KeyError:
            print('Wrong file name or extension')
except FileNotFoundError:
    print('Can`t find this archive')
