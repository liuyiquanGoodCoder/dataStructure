'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，
总共有多少种方法？
'''
class Solution:
    def rectCover(self,number):
        if number <= 2:
            return number
        first,second,third = 1,2,0
        for _ in range(3,number):
            third = first + second
            first = second
            second = third
        return third