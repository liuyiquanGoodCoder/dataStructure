'''
https://cuijiahua.com/blog/2017/12/basis_18.html
'''
class Solution:
    def Mirror(self,root):
        if(root == None or (root.left == None and root.right == None)):
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp

        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)