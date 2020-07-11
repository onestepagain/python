# -*- coding: utf-8 -*-

drinks = ["xu","liu","wang"]
print(drinks)

#查
drinks[0]
drinks[-1]
drinks[0:]

#增
#在末尾添加
drinks.append("pi")

#在任意位置添加
drinks.insert(1,"pi")



#删除
#删除某个元素
del drinks[1]

#pop():弹出尾部元素
drinks.pop()
drinks.pop(1)

#根据值删除元素
drinks.remove("xu")




#改
drinks[0] = ("qi")



#排序:sort方法
cars = ["bmw","audi","dazhong"]
cars.sort()

#sort降序
cars.sort(reverse = True)
print(cars)