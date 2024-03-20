import csv, random

word_list = ['estate', 'concept', 'hurl', 'shark', 'mile', 'sleep', 'researcher']
data_list = []

for word in word_list:
    data_list.append({'word': word, 'num': random.randint(-10, 10)})
# task 4
with open('default.csv', 'w', newline='') as file:
    columns = ['word', 'num']
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(data_list)

with open('default.csv', 'r') as file:
    reader = csv.DictReader(file)
    for i in reader:
        if int(i['num']) > 0:
            print(f"{i['num']} > 0")

with open('default.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = []
    for i in reader:
        print(i['word'], end=' ')
        data.append(i['word'])
    key_word = input(f'\nEnter a key word: ')
    res = []
    for i in data:
        if key_word in i:
            res.append(i)
    print(res)

# task 5
data_list = []
for num in range(7):
    data_list.append({'num': random.randint(11, 20)})

with open('default_num.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['num'])
    writer.writeheader()
    writer.writerows(data_list)

key = 'num'
with open('default.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = []
    for i in reader:
        try:
            data.append({key: i['num']})
        except KeyError:
            print('It does not have this key')
            break

with open('default_num.csv', 'r') as file:
    reader = csv.DictReader(file)
    for i in reader:
        try:
            data.append({key: i['num']})
        except KeyError:
            print('It does not have this key')
            break

with open('combined.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=[key])
    writer.writeheader()
    writer.writerows(data)
