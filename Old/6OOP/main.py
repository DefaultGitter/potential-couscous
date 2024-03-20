class MyClass:
    # var
    # def

    x, y = 10, 40

    def __init__(self, x):  # , y):
        # print('init')
        self.x = x
        # self.y = y

    def getx(self):
        # return self.y
        return self.x

    def setx(self, x):
        # self.y = x
        self.x = x

    def addy(self):
        self.y = 0

    def gety(self):
        return self.y

    @classmethod
    def fu(cls):
        print('hhee',
              cls.x)

    @staticmethod
    def fu2(x, y):
        return x + y


# obj1 = MyClass()
# print(type(obj1))

# print(MyClass.x)
# MyClass.x = 100
# obj1.x = 150
# print(MyClass.x)
# print(obj1.x)

obj1 = MyClass(3)
# obj1.setx(100)
# print(obj1.getx())
# print(obj1.y)
# obj1.z = 77
# print(obj1.z)
# obj1.addy()
# print(obj1.gety())

# print(MyClass.getx(obj1))
print(MyClass.fu2(3, 5))
