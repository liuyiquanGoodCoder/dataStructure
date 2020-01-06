'''
https://cuijiahua.com/blog/2017/12/basis_22.html
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''
class Solution:
    def PrintFromTopToBottom(self,root):
        if not root:
            return []
        result = []
        tmp = [root]
        while len(tmp):
            cur = tmp.pop(0)
            result.append(cur.val)
            if cur.left:
                tmp.append(cur.left)
            if cur.right:
                tmp.append(cur.right)
        return result