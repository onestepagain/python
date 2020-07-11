# -*- coding: utf-8 -*-

import random

num = random.randrange(1,51)
print(num)
cai = int(input())
while num != cai:
    if cai > num:
        print("大了")
    else:
        print("小了")
    cai = int(input())

print("猜对了")
    













