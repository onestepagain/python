# -*- coding: utf-8 -*-



#NameError: name 'a' is not defined【未初始化异常】
#print(a)

"""
怎样解决异常
"""

print(1 / 0)

"""
try except
"""

try:
    print(1 / 0)
except ZeroDivisionError:
    print("0000")



try:
    print(a)
except NameError:
    print("iiiii")








