# -*- coding: utf-8 -*-

#is:判断两个标识符是不是引用自一个对象
stock1 = [1,2,3]
stock2 = stock1
stock2.append(4)
stock3 = stock1.copy()
id(stock1)
id(stock2)
stock1 is stock2
stock1 is stock3





#is not