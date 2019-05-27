class solution:
    def replaceSpace(self,s):
        return s.replace(' ','%20')

string1 = "my book is whose"
obj = solution()
obj.replaceSpace(string1)