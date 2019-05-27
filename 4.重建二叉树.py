class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self,pre,tin):
        if len(pre) == 0:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            pos = tin.index(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:pos+1],tin[:pos])
            root.right = self.reConstructBinaryTree(pre[pos+1:],tin[pos+1:])
        return root

obj = Solution()
pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
tree = obj.reConstructBinaryTree(pre,tin)
print(tree)

def preTraverse(root):  
    '''
    前序遍历
    '''
    if root==None:  
        return  
    print(root.val)  
    preTraverse(root.left)  
    preTraverse(root.right)  

def midTraverse(root): 
    '''
    中序遍历
    '''
    if root==None:  
        return  
    midTraverse(root.left)  
    print(root.val)  
    midTraverse(root.right)  

def afterTraverse(root):  
    '''
    后序遍历
    '''
    if root==None:  
        return  
    afterTraverse(root.left)  
    afterTraverse(root.right)  
    print(root.val) 


midTraverse(tree)
