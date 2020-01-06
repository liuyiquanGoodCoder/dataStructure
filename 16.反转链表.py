'''
https://cuijiahua.com/blog/2017/12/basis_15.html
'''
class Solution:
    def ReverseList(self,pHead):
        if not pHead or not pHead.next:
            return pHead
        last = None
        while pHead:
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last