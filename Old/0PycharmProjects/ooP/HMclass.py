# Створіть простий клас, який надає можливість зберігати рядок.
# Додайте в рядковий клас функцію, яка створює рядок, що містить перетин двох рядків, тобто загальні символи для двох рядків.
# Наприклад, результатом перетину рядків "sdqcg" "rgfas34"
# буде рядок "sg". Для реалізації функції перевантажити оператор * (бінарне множення).

class Simple:
    def __init__(self, text):
        self.text = text

    def __mul__(self, other):
        return ''.join(set(self.text).intersection(set(other.text)))


print(Simple('sdqcg') * Simple('rgfas34'))


# Створити клас Flat (квартира).
# Реалізувати перевантажені оператори:
#     • Перевірка на рівність площ квартир (операція ==);
#     • Перевірка на нерівність площ квартир (операція! =);
#     • Порівняння двох квартир за ціною (операції >,<,<=,>=).

class Flat:
    def __init__(self, superficie, price):
        self.s = superficie
        self.p = price

    def __eq__(self, other):
        return self.s == other.s

    def __ne__(self, other):
        return self.s != other.s

    def __gt__(self, other):
        return self.p > other.p

    def __ge__(self, other):
        return self.p >= other.p

    def __lt__(self, other):
        return self.p < other.p

    def __le__(self, other):
        return self.p <= other.p


h1 = Flat(50, 300)
h2 = Flat(20, 400)

if h1 == h2:
    print('Same area')
elif h1 != h2:
    print('One of them bigger')

if h1 < h2:
    print('First are cheaper')
elif (h1 <= h2) and (h1 >= h2):
    print('They cost the same')
elif h1 > h2:
    print('Second are cheaper')
