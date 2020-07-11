# -*- coding: utf-8 -*-

"""
复制列表
"""

#指向相同内存
stock1 = [1,2,3]
stock2 = stock1
stock2.append(4)
#id()：查看内存地址
id(stock1)
id(stock2)


#重新开辟内存
#1使用列表切片
stock1 = [1,2,3]
stock2 = stock1[:]
stock2.append(4)

#2使用copy()函数
stock1 = [1,2,3]
stock2 = stock1.copy()
stock2.append(5)

