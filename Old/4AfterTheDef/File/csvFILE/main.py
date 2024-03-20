# import csv

# l1 = [
#     ['s1', 's2', 's3'],
#     ['s4', 's5', 's6'],
#     ['s7', 's8', 's9']
# ]
#
# l2 = [
#     {'key1': 'Name1', 'key2': 'age1'},
#     {'key1': 'Name2', 'key2': 'age2'},
#     {'key1': 'Name3', 'key2': 'age3'},
# ]

# with open('file1.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerows(l1)

# with open('file1.csv', 'a', newline='') as file:
#     writer = csv.writer(file, delimiter=',')
#     writer.writerow(['sj', 'body', 'yo'])

# with open('file1.csv', 'r') as file:
#     reader = csv.reader(file)
#     # reader = csv.reader(file, delimiter=';')
#     # print(type(reader))
#     for i in reader:
#         # print(type(i))
#         print(i)

# with open('file2.csv', 'w', newline='') as file:
#     columns = ['key1', 'key2']
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
#     writer.writerows(l2)

# with open('file2.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for i in reader:
#         print(i['key1'])

# import json

# v1 = {'user': {'firstname': 'Dick', 'age': 666, 'size': [19, 4]}}

# s1 = json.dumps(v1)
# d1 = json.loads(s1)
# print(d1['user'])

# with open('file3.json', 'w') as file:
#     json.dump(v1, file)

# with open('file3.json', 'w') as file:
#     file.write(s1)

# with open('file3.json', 'r') as file:
#     re = json.load(file)
#     print(type(re))
#     print(re['user'])

# with open('file3.json', 'r') as file:
#     re2 = file.read()
#     d = json.loads(re2)
#     print(type(re2))
#     print(type(d))
