'''
https://cuijiahua.com/blog/2018/01/basis_32.html
'''
import operator
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if len(numbers) == 0:
            return ''
        compare = lambda a, b:cmp(str(a) + str(b), str(b) + str(a))
        min_string = sorted(numbers, cmp = compare)
        return ''.join(str(s) for s in min_string)

obj = Solution()
a = [3,32,321]
b = obj.PrintMinNumber(a)
print(b)

        