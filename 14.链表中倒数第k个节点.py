'''
https://cuijiahua.com/blog/2017/12/basis_14.html
'''
class Solution:
    def FindKthToTail(self,head,k):
        l = []
        while head:
            l.append(head)
            head = head.next
        if len(l) < k or k < 1:
            return None
        return l[-k]