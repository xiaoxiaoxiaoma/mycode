# -*- coding:utf-8 -*-
class Transform:
    def transformImage(self, mat, n):
        # write code here

        #把列表倒排一遍
        #b=['1','2','3','4','5','6']
        #for i in range(len(b)-1,-1,-1):
        #b.append(b[i])
        mat.reverse()

        for i in range(n):
            for j in range(i, n):
                if i == j:
                    pass
                else:
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        return mat