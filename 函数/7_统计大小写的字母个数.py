# -*- coding: utf-8 -*-

def count_num(str_in):
    upper, lower = 0, 0
    for i in str_in:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        else:
            continue
    return upper, lower
    

strs = input()
upper, lower = count_num(strs)
print(upper)
print(lower)







#统计大小写单词
def nums_count(splited):
    upper,lower = 0, 0
    for word in splited:
        l = word.lstrip("“")
        if l[0].isupper():
            upper += 1
        elif l[0].islower():
            lower += 1
        else:
            continue
    return upper, lower
        
        
juzi = "Internet has been playing an increasingly important role in our day-to-day life. It has brought a lot of benefits but has created some serious problems as well."
splited = juzi.split()
upper, lower = nums_count(splited)
print(upper)
print(lower)























