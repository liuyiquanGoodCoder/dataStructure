'''
https://cuijiahua.com/blog/2017/12/basis_20.html
定义栈的数据结构，
请在类型中实现一个能够得到栈最小元素的min函数
'''
class Solution:
    def __init__(self):
        self.Data = []
        self.Min = []
    def push(self,node):
        self.Data.append(node)
        if self.Min:
            if self.Min[-1] > node:
                self.Min.append(node)
            else:
                self.Min.append(self.Min[-1])
        else:
            self.Min.append(node)
    def pop(self):
        if self.Data == []:
            return None
        self.Min.pop()
        return self.Data.pop()
    def top(self):
        if self.Data == []:
            return None
        return self.Data[-1]
    def min(self):
        if self.Min == []:
            return None
        return self.Min[-1]