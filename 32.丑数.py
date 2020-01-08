'''
https://cuijiahua.com/blog/2018/01/basis_33.html
'''
class Solution:
    def GetUglyNumber_Solution(self,index):
        if index < 7:
            return index
        res = [1,2,3,4,5,6]
        t2,t3,t5 = 3,2,1
        for i in range(6,index):
            res.append(min(res[t2] * 2,min(res[t3]*3,res[t5]*5)))
            while res[t2]*2 <= res[i]:
                t2 += 1
            while res[t3]*3 <= res[i]:
                t3 += 1
            while res[t5]*5 <= res[i]:
                t5 += 1
        return res

obj = Solution()
a = 12
b = obj.GetUglyNumber_Solution(a)
print(b)
print(b[a-1])