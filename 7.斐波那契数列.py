class Solution:
    def fibonacci(self,n):
        if n <= 1:
            return 
        first, second, third = 0, 1, 0
        for i in range(2,n+1):
            third = first + second
            first = second
            second = third
        return third

obj = Solution()
obj.fibonacci(10)