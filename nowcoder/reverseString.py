# 题目描述
#
# 请实现一个算法，在不使用额外数据结构和储存空间的情况下，翻转一个给定的字符串(可以使用单个过程变量)。
#
# 给定一个string iniString，请返回一个string，为翻转后的字符串。保证字符串的长度小于等于5000。
# 测试样例：
#
# "This is nowcoder"
#
# 返回："redocwon si sihT"



# -*- coding:utf-8 -*-
class Reverse:
    def reverseString(self, iniString):
        # write code here
        b = []
        for i in range(len(iniString) - 1, -1, -1):
            b.append(iniString[i])
        return b


if __name__ == '__main__':
    re = Reverse()
    a = re.reverseString(input())
    c=''.join(a)
    print(c)
