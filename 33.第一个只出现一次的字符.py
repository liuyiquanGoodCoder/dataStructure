'''
在一个字符串(1<=字符串长度<=10000，
全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置。
https://cuijiahua.com/blog/2018/01/basis_34.html
'''
class Solution:
    def FirstNotRepeatingChar(self,s):
        length = len(s)
        if length == 0:
            return -1
        item = {}
        for i in range(length):
            if s[i] not in item.keys():
                item[s[i]] = 1
            else:
                item[s[i]] += 1
        for i in range(length):
            if item[s[i]] == 1:
                return i
        return -1

obj = Solution()
a = 'aabbbccdd'
b = obj.FirstNotRepeatingChar(a)
print(b)

