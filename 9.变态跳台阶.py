'''
一只青蛙一次可以跳上1级台阶，
也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
class Solution:
    def jumpfloorcrazy(self,number):
        if number <= 2:
            return number
        total = 1
        for _ in range(1,number):
            total *= 2
        return total


obj = Solution()
obj.jumpfloorcrazy(5)