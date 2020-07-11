# -*- coding: utf-8 -*-

#./:当前目录   ../:上一层目录
#f = open("C:/Users/joker/Desktop/古诗.txt", mode = 'r', encoding='UTF-8')
#f = open("C:/Users/joker/Desktop/古诗.txt")
#f = open("./古诗.txt", mode = 'r', encoding='UTF-8')
f = open(r"C:\Users\joker\Desktop\古诗.txt", mode = 'r', encoding='UTF-8')
content = f.read()
print(content)
f.close()



#一行一行读取
f = open(r"C:\Users\joker\Desktop\古诗.txt", mode = 'r', encoding='UTF-8')
content = f.readline().strip()
content2 = f.readline().strip()
f.flush()#刷新
f.close()


#将每一行形成一个元素，置于列表里面
#一行一行读取
f = open(r"C:\Users\joker\Desktop\古诗.txt", mode = 'r', encoding='UTF-8')
content = f.readlines()
f.flush()#刷新
f.close()


#逐行读取
#一行一行读取
f = open(r"C:\Users\joker\Desktop\古诗.txt", mode = 'r', encoding='UTF-8')
for line in f:
    print(line.strip())
f.flush()#刷新
f.close()





#读pdf
f = open(r"C:\Users\joker\Desktop\Java复习笔记.pdf", 
    mode = 'rb')
content = f.read()
f.close()



