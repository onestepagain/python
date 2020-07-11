# -*- coding: utf-8 -*-

import time

dir(time)


"""
打印当前的时间
"""
now = time.time()
print(now)


"""
计算某个程序运行的时间
"""
def sum1(times):
    z = 0
    for i in range(1, times + 1):
        z += i
    return z

start_time = time.time()
result = sum1(10000000)
end_time = time.time()
print(end_time - start_time)


"""
延时打印
"""
for i in range(3):
    print("h")
    time.sleep(1)






















