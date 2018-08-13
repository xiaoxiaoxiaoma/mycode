# # -*- coding:utf-8 -*-
# class ReverseEqual:
#     def checkReverseEqual(self, s1, s2):
#         # write code here
#         if set(s1) != set(s2) or len(s1) != len(s2):
#             return 'false'
#         else:
#             a = list(set(s1))
#             b = list(set(s2))
#             for i in a:
#                 if list(s1).count(i) == list(s2).count(i):
#                     pass
#                 else:
#                     return 'false'
#             else:
#                 return 'true'
#
# if __name__ == '__main__':
#     s1,s2 = input().split(",")
#     re = ReverseEqual()
#     a = re.checkReverseEqual(s1,s2)
#     print(a)

'''
以s1=ABCD为例，我们先分析s1进行循环移位之后的结果：
ABCD->BCDA->CDAB->DABC->ABCD  .......
假设我们把前面移走的数据进行保留：
ABCD->ABCDA->ABCDAB->ABCDABC->ABCDABCD.....
因此看出，对s1做循环移位，所得字符串都将是字符串s1s1的子字符串。如果s2可以由s1循环移位得到，则一定可以在s1s1上
'''
class ReverseEqual:
    def checkReverseEqual(self, s1, s2):
        # write code here
        if len(s1)==0 or len(s2)==0:
            return False
        else:
            s3 = s1 + s1
            if s2 in s3:
                return True
            else:
                return False
