class Test:
    def __init__(self, var):
        self.__var = var

    def __str__(self):
        return 'Word'

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    def getvar(self):
        return self.__var


# with Test(5) as test:
#     print(test.getvar())
#     print(test)


class Point2D:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        # print('init')

    def __str__(self):
        return f'x = {self.__x}, y = {self.__y}'

    # def __del__(self):
    #     print('del')

    def setX(self, x):
        self.__x = x

    def getX(self):
        return self.__x

    def __add__(self, other):
        tmpX = self.__x + other.__x
        tmpY = self.__y + other.__y
        return Point2D(tmpX, tmpY)

    def __int__(self):
        print('int')

    def __iadd__(self, other):
        self.__x += other
        # self.__y += other
        return self

    def __getitem__(self, item):
        if item.getX() == 30:
            return self.__x
        # if item in [1, 'x']:
        #     return self.__x
        # elif item in [2, 'y']:
        #     return self.__y

    def __setitem__(self, key, value):
        if key == 1:
            self.__x += value
        elif key == 2:
            self.__y += value


p1 = Point2D(30, 50)
p2 = Point2D(20, 40)

# print(p1)
# p1.setX(p2.getX())
# print(p1)
p3 = p1 + p2
# print(p1)
print(p3)
# p1 += 1
# print(p1)

# print(p1[1])
# print(p1[Point2D(30, 2)])

p1[1] = 100
print(p1)
