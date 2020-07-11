# -*- coding: utf-8 -*-

"""
zip() ->迭代器
将我们给定的数据（可迭代对象）中对用的元素打包成一个元组
可迭代对象：字符串、列表、元组、字典
"""
fruits = ["apple", "banana", "peach"]
prices = [10, 8, 9]
colors = ["green", "yellow", "red"]
result = list(zip(fruits, prices, colors))
print(result)



fruits = ["apple", "banana", "peach"]
prices = [10, 8, 9]
colors = ["green", "yellow", "red"]

for fruit, price in zip(fruits, prices):
    print(fruit, price)









