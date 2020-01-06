'''
https://cuijiahua.com/blog/2017/12/basis_17.html
'''
class Solution:
    def HasSubtree(self,pRoot1,pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        return self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2) or self.is_subtree(pRoot1,pRoot2)

    def is_subtree(self,Root1,Root2):
        if not Root2:
            return True
        if not Root1 or Root1.val != Root2.val:
            return False
        return self.is_subtree(Root1.left,Root2.left) and self.is_subtree(Root1.right,Root2.right)