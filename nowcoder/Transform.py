# -*- coding:utf-8 -*-
class Transform:
    def transformImage(self, mat, n):
        # write code here
        m=n
        for i in range(n-1,-1,-1):
            for j in range(n):
                mat[m].append(mat[i][j])
            m+=1
        for i in range(n):
            mat.pop(0)
        return mat
# I need more time to solve it