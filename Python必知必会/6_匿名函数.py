# -*- coding: utf-8 -*-

"""
匿名函数：lambda

"""

sum1 = lambda x, y:x + y
print(sum1(1, 2))

sum2 = lambda x, y, z: x + y + z
print(sum2(1, 2, 3))




"""
添加条件表达式：只能添加条件表达式（匿名函数的极限）
"""

func2 = lambda x:"ok" if x == 1 else "no"
func2(0)


"""
map():
语法：
map(function, iterable, ...)
function:函数
iterable:添加一个或者多个序列
"""
def square(x):
    return x ** 2
data = list(range(0, 11))

print(list(map(square, data)))
print(list(map(lambda x: x ** 2, data)))
print(list(map(lambda x, y: x + y, data, data)))











