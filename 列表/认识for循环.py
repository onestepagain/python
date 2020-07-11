# -*- coding: utf-8 -*-

drinks = ["mai","ke","fen","qi"]

print(drinks[0])
"""
冒号不能省略
缩进问题。
"""
for drink in drinks:
    print("饮料：")
    print(drink)

i = 1
for drink in drinks:
    print("周{}用".format(i) + drink + ".")
    i += 1;