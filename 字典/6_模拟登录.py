# -*- coding: utf-8 -*-

loading = {"111":"111", "222":"222", "333":"333"}

name = input()
password = input()

if password == loading.get(name):
    print("成功")
else:
    print("失败")



name = input()
password = input()

if name not in list(loading.keys()):
    print("未注册")













