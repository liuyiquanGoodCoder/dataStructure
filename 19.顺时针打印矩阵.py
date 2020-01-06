'''
https://cuijiahua.com/blog/2017/12/basis_19.html
'''
class Solution:

    def printMatrix(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        if rows == 0 and cols == 0:
            return result
        left,right,top,bottom = 0,cols - 1,0,rows-1
        while left <= right and top <= bottom:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            for i in range(top+1,bottom+1):
                result.append(matrix[i][right])
            if top != bottom:
                for i in range(left,right)[::-1]:
                    result.append(matrix[bottom][i])
            if left != right:
                for i in range(top+1,bottom)[::-1]:
                    result.append(matrix[i][left])
            left += 1
            top += 1
            right -= 1
            bottom -= 1
        return result
'''
给定一个数字，打印矩阵
'''
def matrix(target):
    num = target * target
    left,right,top,bottom = 0,target-1,0,target-1
    res = [[0 for col in range(target)] for row in range(target)]
    each = 1
    while left <= right and top <= bottom and each <= num:
        for i in range(left,right+1):
            res[top][i] = each
            each += 1
        for i in range(top+1,bottom+1):
            res[i][right] = each
            each += 1
        if top != bottom:
            for i in range(left,right)[::-1]:
                res[bottom][i] = each
                each += 1
        if left != right and each <= num:
            for i in range(top+1,bottom)[::-1]:
                res[i][left] = each
                each += 1
        top += 1
        left += 1
        bottom -= 1
        right -= 1
    for i in range(len(res)):
        print("\t".join('%s' %id for id in res[i]))


if __name__ == '__main__':
    matrix(4)