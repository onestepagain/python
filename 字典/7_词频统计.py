# -*- coding: utf-8 -*-

#字符串的处理方式
#去除左空格
str1 = "  abc"
str1 = str1.lstrip()
print(str1)

#去除右空格
str2 = "abc   "
str2 = str2.rstrip()
print(str2)


#取出左右空格
str3 = "  abc   "
str3 = str3.strip()
print(str3)



#去除左右指定的字符
str4 = "abc,"
str4 = str4.strip(",")
print(str4)


long_str = "Internet has been playing an increasingly important role in our day to day life. It has brought a lot of benefits but has created some serious problems as well."

#将字符串转换为小写
long_str = long_str.lower()
#切分字符串
split_result = long_str.split()
#定义储存字典
result = {}
#遍历切分后的结果
for word in split_result:
    l = word.strip()
    l = word.strip(".")
    result[l] = result.get(l,0) + 1

print(result)









