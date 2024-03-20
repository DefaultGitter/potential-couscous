def fn_test():
    """
    empty func\n
    do nothing
    :return: hhh
    """
    pass


fn_test()

x, y = 0, 1

# def fn_tt(var: int):
#     global x
#     print(var)
#     x = 10
#     y = 100
# fn_tt(32)
# print(x, y)

# def fn_master(var=0):
#     def fn_sub():
#         print("fff")
#     fn_sub()
# fn_master()

# def fn_test(v1, *, v2=0, v3=None):        # строгая передача по имени после *
# def fn_test(v1, v2=0, /, v3=None):        # строгая передеача по позиции до /
# def fn_test(v1, v2=0, /, *, v3=None):     # тупо, но можно
#     print(v3)
#     return v1 + v2
# print(fn_test(v2=0, v1=3))
# print(fn_test(0, v3=3, v2=9))
# print(fn_test(0, 9, v3=3))

# def fn_fff(*var):                         # передача множества параметров
#     for i in var:                         # var is list
#         print()
# fn_fff(2,4,6,9)

# * args | ** kvargs
