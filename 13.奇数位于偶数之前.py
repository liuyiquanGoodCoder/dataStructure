'''
双向队列
'''
'''
from collections import deque
class Solution:
    def reOrderArray(self,array):
        odd = deque()
        l = len(array)
        for i in range(l):
            if array[l-i-1] % 2 != 0:
                odd.appendleft(array[-i-1])
            if array[i] % 2 == 0:
                odd.append(array[i])
        return list(odd)

'''
'''
列表
'''
'''
class Solutionform:
    def reOrderArray(self,array):
        res = []
        l = len(array)
        for i in range(l):
            if array[l-i-1]%2 != 0:
                res.insert(0,array[-i-1])
            if array[i] % 2 ==0:
                res.append(array[i])
        return res
'''
'''
不开辟新空间
'''
class Solution:
    def reOrderArray(self,array):
        boarder = -1
        for idx in range(len(array)):
            if array[idx] % 2:
                boarder += 1
                array.insert(boarder,array.pop(idx))
        return array

obj = Solution()
a = [3,5,4,1,6,7,8,9,11,12,6,7,8,19]
obj.reOrderArray(a)



