'''
https://cuijiahua.com/blog/2017/12/basis_30.html
'''
class Solution:
    def FindGreatestSumOfSubArray(self,array):
        if len(array) == 0:
            return 0
        maxSum = array[0]
        curSum = array[0]

        for each in array[1:]:
            if curSum <= 0:
                curSum = each
            else:
                curSum += each
            if curSum > maxSum:
                maxSum = curSum
        return maxSum