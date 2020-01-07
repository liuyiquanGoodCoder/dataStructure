'''
https://www.nowcoder.com/profile/5943283/codeBookDetail?submissionId=11158671
'''
import collections
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        tmp = collections.Counter(numbers)
        x = len(numbers)/2
        for k, v in tmp.items():
            if v > x:
                return k
        return 0


obj = Solution()
a = [1,2,5,5,5,5,5,8,9]
b = obj.MoreThanHalfNum_Solution(a)
print(b)
        