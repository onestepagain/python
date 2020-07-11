# -*- coding: utf-8 -*-

def greet(name):
    print(name)
greet("libai")


#复杂点的


#关键字实参
#可以指定传入参数的顺序



#使用默认值
def greet(name, gender = "female"):
    print(name)
    if(gender == "female"):
        print("nv")
    else:
        print("nan")
    
greet("libai")
greet("libai", "male")










