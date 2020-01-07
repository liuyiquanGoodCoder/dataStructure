'''
https://cuijiahua.com/blog/2017/12/basis_31.html
'''
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        ones, m = 0, 1
        while m <= n:
            ones += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
            m *= 10
        return ones
obj = Solution()
b = 12
a = obj.NumberOf1Between1AndN_Solution(b)
print(a)