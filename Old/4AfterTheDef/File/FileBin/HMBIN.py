import shelve
import pickle


def make_an_order():
    order = {}
    print('\nPress enter to finish placing your order')
    while True:
        while True:
            _product = input('\nEnter a name of position: ')
            if _product.title() in product_list.keys() or not _product:
                break
            print('Sorry, but we do not have this position right now.'
                  '\nPlease, chose another product')

        if not _product:
            break

        while True:
            try:
                num = int(input('Enter a number of goods: '))
                break
            except ValueError:
                print('Wrong input')

        _product = _product.title()
        order[_product] = product_list[_product] * num

    return order


product_list = {}
with shelve.open('price_list') as file:
    for key in file:
        product_list[key] = file[key]

for product in product_list:
    print(f'"{product}" cost {product_list[product]}')

receipt = make_an_order()

total_price = 0
with open('sales_receipt.bin', 'wb') as file:
    for goods in receipt.keys():
        pickle.dump(goods, file)
        total_price += receipt[goods]
    pickle.dump(f'Total price is: {total_price}', file)

with open('sales_receipt.bin', 'rb') as file:
    line = ' '
    print('\nYou`ve ordered: ')
    while line:
        try:
            line = pickle.load(file)
            print(line)
        except EOFError:
            break
