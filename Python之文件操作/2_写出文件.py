# -*- coding: utf-8 -*-

"""
(1)删除原始文件内的内容，重新写入
(2)可以创建没有的文件
"""
f = open(r"C:\Users\joker\Desktop\古诗1.txt",
     mode = 'w', encoding = 'utf8')
f.write("李白")
f.flush()
f.close()


"""
批量写出文件
"""
def out(num):
    for i in range(num + 1):
        path = r"C:\Users\joker\Desktop\古诗\古诗" + str(i) + ".txt"
        f = open(path, mode = 'w', encoding = 'utf8')
        f.write("(1)删除原始文件内的内容，重新写入\
                (2)可以创建没有的文件")
        f.flush()
        f.close()
        
out(10)



#mode = 'a'  :追加数据
f = open(r"C:\Users\joker\Desktop\古诗1.txt",
     mode = 'a', encoding = 'utf8')
f.write("啊")
f.flush()
f.close()





#mode = 'wb':写出文件，可以不用指定打开文件的编码
"""
前提：在我们写出文件的时候，一定要指定写出字符串的编码
"""
f = open(r"C:\Users\joker\Desktop\古诗1.txt",
     mode = 'wb')
f.write("静夜思".encode('utf8'))
f.flush()
f.close()



#mode = 'r+' :既可以读，也可以写 - 必须先读再写 -在原基础上追加写
f = open(r"C:\Users\joker\Desktop\古诗1.txt",
     mode = 'r+', encoding = 'utf8')
content = f.read()
f.write("李白")
print(content)
f.flush()
f.close()









