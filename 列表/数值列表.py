# -*- coding: utf-8 -*-

#range()函数      左闭右开
for i in range(1,11):
    print(i)
    
    
nums = list(range(1,11))
print(nums)

for i in range(0,11,2):
    print(i)
    
    
#计算数字1-10的平方和
sum = 0
for i in range(1,11):
    value = i ** 2
    sum += value
print(sum)