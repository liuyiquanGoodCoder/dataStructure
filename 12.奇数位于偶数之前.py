'''
双向队列
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
列表

class Solutionform:
    def reOrderArray(self,array):
        res = []
        l = len(array)
        for i in range(l):
            if array[l]:
                pass
            else:
                pass
'''