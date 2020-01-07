'''
输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，
则最小的4个数字是1,2,3,4。

class Solution:
    def GetLeastNumbers_Solution(self,tinput,k):
        if len(tinput) < k:
            return []
        tmp = sorted(tinput[:k])
        for each in tinput[k:]:
            index = k - 1
            flag = False
            while index >= 0 and tmp[index] > each:
                index -= 1
                flag = True
            if flag == True:
                tmp.insert(index+1,each)
                tmp.pop()
        return tmp
'''
class Solution:
    def HeadAdjust(self,input_list,parent,length):
        temp = input_list[parent]
        child = 2 * parent + 1
        while child < length:
            if child + 1 < length and input_list[child] < input_list[child+1]:
                child += 1
            if temp >= input_list[child]:
                break
            input_list[parent] = input_list[child]
            parent = child
            child = 2 * parent + 1
        input_list[parent] = temp
    
    def GetLeastNumbers_Solution(self,tinput,k):
        res = []
        length = len(tinput)
        change = True
        if length <= 0 or k <= 0 or k > length:
            return res
        res = tinput[:k]

        for i in range(k,length+1):
            if change == True:
                for j in range(0,k//2+1)[::-1]:
                    self.HeadAdjust(res,j,k)
                for j in range(1,k)[::-1]:
                    res[0],res[j] = res[j],res[0]
                    self.HeadAdjust(res, 0, j)
                change = False
            if i != length and res[k-1] > tinput[i]:
                res[k-1] = tinput[i]
                change = True
        return res
            
