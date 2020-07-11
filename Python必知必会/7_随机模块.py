# -*- coding: utf-8 -*-

import random

#生成0~1内的随机数
num = random.random()
print(num)


#随机种子
"""
保证产生的随机数是一样的
伪随机数，根据unix时间来确定的
"""
random.seed(100)
num = random.random()
print(num)



#产生一个包含上下界限的随机整数
"""
random.randint(a, b)
"""
num = random.randint(0, 10)
print(num)


"""
random.randrange(start, stop, step)
按步长随即在上下范围内选择一个随机数
"""
num = random.randrange(20, 100, 5)
print(num)


"""
random.uniform(a, b)
取a，b范围内的一个小数
"""
num = random.uniform(1, 2)
print(num)



"""
随机选取：
sample
choice
"""
print(random.sample("12345",2))
print(random.choice("1234"))

"""
洗牌
shuffle
"""
nums = [1, 2, 3, 4, 5]
print(nums)
random.shuffle(nums)
print(nums)








