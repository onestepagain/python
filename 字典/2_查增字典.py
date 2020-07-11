# -*- coding: utf-8 -*-

person = {"name":"peter", "age":24, "gender":"male"}
print(person)

#访问字典
print(person["name"])

#得到所有的键值 keys()
for key in person.keys():
    print(key)

#得到所有的值  values()
for value in person.values():
    print(value)
    
#同时得到所有的键值对   items

a = []
b = []
for key, value in person.items():
    a.append(key)
    b.append(value)
    
print(a)
print(b)


#增
person["height"] = 175
      
      
print(len(person))





























