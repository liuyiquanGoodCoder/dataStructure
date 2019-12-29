class Solution:
    def Power(self,base,exponent):
        flag = 0
        result = 1
        if base == 0:
            return False
        if exponent < 0:
            flag = 1
        for _ in range(abs(exponent)):
            result *= base
        if flag == 1:
            result = 1 / result
        return result