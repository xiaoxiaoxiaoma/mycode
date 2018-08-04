# coding = utf-8
f = open("C:\data\log1","w",encoding="UTF-8")

# 读取文件的所有内容，read（size）
# size被忽略了或者为负，返回所有内容；若不为空，则返回一定数目的字节
# str = f.read()
# print(str)

#读取文件的一行
#换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行
# str = f.readline()
# print(str)

#f.readlines()将返回该文件中包含的所有行
#如果设置可选参数sizehint，则读取指定长度的字节，并且将这些字节按行分割
# str = f.readlines(15)
# print(str)

#迭代一个文件对象然后读取每行
# for line in f:
#     print(line,end='')


#往文件中写入string,返回写入的字符数68
# num = f.write("python is nice! Now i learn it, and i want to use it to do something")
# print(num)

#如果要写入一些不是字符串的东西，那么将需要先进行转换
value = ('www.runoob.com',14)
s = str(value)
f.write(s)

f.close()