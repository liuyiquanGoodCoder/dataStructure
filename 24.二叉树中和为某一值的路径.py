'''
https://cuijiahua.com/blog/2017/12/basis_24.html
'''
class Solution:
    def FindPath(self,root,expectNumber):
        if not root:
            return []
        if not root.left and not root.right and expectNumber == root.val:
            return [[root.val]]
        res = []
        left = self.FindPath(root.left,expectNumber-root.val)
        right = self.FindPath(root.right,expectNumber-root.val)
        for i in left+right:
            res.append([root.val]+i)
        return res

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

if __name__ =='__main__':
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(3)
    A4 = TreeNode(4)
    A5 = TreeNode(5)
    A6 = TreeNode(6)

    A1.left = A2
    A1.right = A3
    A2.left = A4
    A2.right = A5
    A4.left = A6

    solution = Solution()
    ans = solution.FindPath(A1,8)
    print('ans=',ans)