# class Test:
#     def __init__(self):
#         self.lst = [10, 22, 35, 17]
#
#     def __iter__(self):
#         return self.lst.__iter__()
#         return iter(self.lst)


# tt = Test()
# for i in tt:
#     print(i)

# lst = [10, 22, 35, 17]
# re = iter(lst)
# while True:
#     try:
#         print(re.__next__())
#     except:
#         break


class Point2D:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def setx(self, x):
        self.__x = x

    def sety(self, y):
        self.__y = y

    def __str__(self):
        return f'x = {self.__x}, y = {self.__y}'

    # def testfn(self):
    #     print('fn')


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z

    def __str__(self):
        # return f'x = {self.getx()}, y = {super().gety()}, z = {self.__z}'
        return f'{super().__str__()}, z = {self.__z}'


# x = Point3D(1,2)
# x.testfn()

p1 = Point3D(1, 2, 3)
# p1.sety(3)
# print(p1.gety())

print(p1)
