'''
https://cuijiahua.com/blog/2017/12/basis_21.html
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
'''
class Solution:
    def IsPopOrder(self,pushV,popV):
        if len(popV) == 0 or len(pushV) != len(popV):
            return False
        stackData = []
        for i in pushV:
            stackData.append(i)
            while len(stackData) and stackData[-1] == popV[0]:
                stackData.pop()
                popV.pop(0)
        if len(stackData):
            return False
        return True