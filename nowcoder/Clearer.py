# -*- coding:utf-8 -*-
#注意若 row=column=set(),这说明row和column所指向的内存区域是相同的
class Clearer:
    def clearZero(self,mat,n):
        row = set()
        column = set()
        for i in range(n):
            for j in range(n):
                if mat[i][j] == 0:
                    row.add(i)
                    column.add(j)

        for i in list(row):
            for z in range(n):
                mat[i][z] = 0

        for i in list(column):
            for z in range(n):
                mat[z][i] = 0
        return mat

if __name__ == '__main__':
    a = [[1,2,3],[0,1,2],[0,0,1]]
    b = 3
    cc = Clearer()
    d = cc.clearZero(a,b)
    print(d)
