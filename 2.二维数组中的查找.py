class Solution:
    def Find(self,target,array):
        rows = len(array)
        cols = len(array[0])
        if rows > 0 and cols > 0:
            row = 0
            col = cols - 1
            while row < rows and col >= 0:
                if target == array[row][col]:
                    return True
                elif target < array[row][col]:
                    col -= 1
                else:
                    row += 1
        return False
array = [[1,2,3],[4,5,6],[7,8,9]]
obj = Solution()
obj.Find(10,array)