# -*- coding:utf-8 -*-
class Zipper:
    def zipString(self, iniString):
        # write code here
        a = []
        n = 1
        c=''
        for i in range(1, len(iniString)-1):
            if iniString[i-1] == iniString[i]:
                n += 1
            else:
                a.append(iniString[i-1])
                a.append(n)
                n = 1
        if iniString[-1] == iniString[-2]:
            a.append(iniString[-1])
            a.append(n+1)
        for i in a:
            c=c+str(i)
        if len(iniString) > len(c):
            return c
        else:
            return iniString

if __name__ == '__main__':
    ini = input("Please:")
    ini = ini[1:-1]
    zipper = Zipper()
    zipper.zipString(ini)