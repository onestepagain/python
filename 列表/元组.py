# -*- coding: utf-8 -*-

"""
元组内元素无法修改，以圆括号括起来
"""

location = (1,2,3)
print(location)

location[0] = 10
print(location)

#重新创建新元组覆盖旧元组即可
location = (10,2,3)
print(location)

#遍历元组
for i in location:
    print(i)