# -*- coding: utf-8 -*-


"""
通过指定的分隔符对字符串进行分割
第一个参数：（指定分隔符）
第二个参数：切成几份
"""

song = "the day you went away"
result = song.split()
print(result)

song = "the|day|you|went|away"
result = song.split("|")
print(result)

song = "the|day|you|went|away"
result = song.split("|",1)
print(result)
