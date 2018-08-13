# -*- coding:utf-8 -*-
class ReverseEqual:
    def checkReverseEqual(self, s1, s2):
        # write code here
        if set(s1) != set(s2) or len(s1) != len(s2):
            return 'false'
        else:
            a = list(set(s1))
            b = list(set(s2))
            for i in a:
                if list(s1).count(i) == list(s2).count(i):
                    pass
                else:
                    return 'false'
            else:
                return 'true'

if __name__ == '__main__':
    s1,s2 = input().split(",")
    re = ReverseEqual()
    a = re.checkReverseEqual(s1,s2)
    print(a)