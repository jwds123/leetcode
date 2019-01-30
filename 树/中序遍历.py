# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        if root==None:
            return res
        if root.left!=None:
            res+=self.inorderTraversal(root.left)
        if root.val!=None:
            res.append(root.val)
        if root.right!=None:
            res+=self.inorderTraversal(root.right)

        return res
