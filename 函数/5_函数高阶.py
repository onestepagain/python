# -*- coding: utf-8 -*-

"""
传递列表：
"""
def greet(names):
    for name in names:
        msg = "Hello, "
        print(msg + name.title())

names = ["111", "222"]
greet(names)



"""
传递任意数量的实参
*表示传递任意数量的实参
存储在元组中
"""
def make_pizza(*topplings):
    print(topplings)

make_pizza("1")
make_pizza("1","2")



