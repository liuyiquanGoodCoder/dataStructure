class Solution:
    def jumpFloor(self,number):
        if number < 3:
            return number 
        first,second,third = 1,2,0
        for _ in range(3,number+1):
            '''
            print(i)
            '''
            third = first + second
            first = second
            second = third
        return third

obj = Solution()
obj.jumpFloor(5)