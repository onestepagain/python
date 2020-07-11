# -*- coding: utf-8 -*-

"""
返回值：
1.可以返回任意类型的值
"""

#小例子
def get_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

person = get_name("lebron", "james")
print(person)













