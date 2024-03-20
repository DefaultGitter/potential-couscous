import shelve
import pickle


def make_an_order():
    order = {}
    while True:
        while True:
            product = input('\nEnter a name of position: ')
            if product.title() in product_list.keys() or not product:
                break
            print('Sorry, but we do not have this position right now.'
                  '\nPlease, chose another product')

        if not product:
            break

        while True:
            try:
                num = int(input('Enter a number of goods: '))
                break
            except ValueError:
                print('Wrong input')

        product = product.title()
        order[product] = product_list[product] * num

    return order


product_list = {}
with shelve.open('price_list') as file:
    for key in file:
        product_list[key] = file[key]

receipt = make_an_order()
total_price = 0
with open('sales_receipt.bin', 'wb') as file:
    for goods in receipt.keys():
        pickle.dump(goods, file)
        total_price += receipt[goods]

with open('sales_receipt.bin', 'rb') as file:
    # line = pickle.load(file)
    # print(line)
    line = ' '
    while line:
        try:
            line = pickle.load(file)
            print(line)
        except EOFError:
            break
