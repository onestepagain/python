# -*- coding: utf-8 -*-

"""
用到马青公式
计算圆周率时为了避免浮点数的不精确问题，
将小数转换为整数计算
"""
#首先指定计算多少个小数
number = 1000
#多计算十位，为了防止尾数出现取舍的影响
number1 = number + 10
#定义计算小数的位数
b = 10 ** number1
#求首项的小数
x1 = b * 4 // 5
x2 = b * 1 // -239
he = x1 + x2
#循环中止条件
number = number * 2
for i in range(3, number, 2):
    x1 //= -25;
    x2 //= (-239 * 239)
    x = (x1 + x2) // i
    he = he + x
#得到pai
pai = he * 4
#去掉多计算的10为
pai //= 10 ** 10
str_pai = str(pai)
#转换为浮点状态
result = str_pai[0] + '.' + str_pai[1:]
#写出文件
with open("pai.txt",
     mode = 'w', encoding = 'utf8') as f:
    f.write(result)
    



"""
测试
"""





