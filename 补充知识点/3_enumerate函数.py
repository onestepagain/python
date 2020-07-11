# -*- coding: utf-8 -*-

"""
用于一个可遍历的对象（列表，字符串，元组）
组合为一个带索引的元素，需使用list()将数据从索引取出
"""

fruits = ["apple", "banana", "peach"]
indexs = list(range(len(fruits)))
#list(zip(index, fruits))

for index, fruit in zip(indexs, fruits):
    print(index, fruit)




#enumerate()函数
#list(enumerate(fruits))

for index,fruit in enumerate(fruits):
    print(index, fruit)











