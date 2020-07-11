# -*- coding: utf-8 -*-

fruits = ["apple", "banana", "peach"]
prices = [10, 8, 9]
result = list(zip(fruits, prices))
print(result)

#解压
huans = list(zip(*result))
lists = []
for huan in huans:
    lists.append(list(huan))

















