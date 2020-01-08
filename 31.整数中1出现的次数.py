'''
https://cuijiahua.com/blog/2017/12/basis_31.html
'''
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        i = 1
        while i <= n:
            a = n / i
            b = n % i
            print(b)
            count += (a+8) / 10 * i + (a % 10 == 1)*(b + 1)
            #print(count)
            i *= 10
        return count
obj = Solution()
b = 12
a = obj.NumberOf1Between1AndN_Solution(b)
print(a)