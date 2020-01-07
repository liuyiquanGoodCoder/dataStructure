'''
    输入一个字符串,按字典序打印出该字符串中字符的所有排列。
    例如输入字符串abc，则打印出由字符a,b,c所能排列出来的所有字符串
    abc,acb,bac,bca,cab和cba。
'''
class Solution:
    def __init__(self):
        self.result = []
    def Permutation(self,ss):
        if len(ss) == 0:
            return []
        self.PermutationCore(ss,0)
        sorted(self.result)
        return self.result
    def PermutationCore(self,str_,begin):
        if begin == len(str_):
            self.result.append(str_)
            return
        for i in range(begin,len(str_)):
            if i != begin and str_[i] == str_[begin]:
                continue
            str_list = list(str_)
            str_list[i],str_list[begin] = str_list[begin],str_list[i]
            str_ = ''.join(str_list)
            self.PermutationCore(str_,begin+1)
'''
class Solution:
    def Permutation(self,ss):
        if len(ss) <= 0:
            return []
        res = list()
        self.perm(ss,res,'')
        uniq = list(set(res))
        return sorted(uniq)
    def perm(self,ss,res,path):
        if ss == '':
            res.append(path)
        else:
            for i in range(len(ss)):
                self.perm(ss[:i]+ss[i+1:],res,path+ss[i])
'''
obj = Solution()
a = 'abc'
b = obj.Permutation(a)
print(b)
