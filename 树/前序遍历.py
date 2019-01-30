class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        root->left->right
        """
        if root is None:
            return []
        res = []
        tmp = []
        tmp.append(root)
        while tmp:
            node = tmp.pop()  # 先进后出；所以right-left
            res.append(node.val)  # 先加入根节点的值，再加入左右子树
            if not node.right:
                tmp.append(node.right)
            if not node.left:
                tmp.append(node.left)
        return res

        # 超时
        # res = []
        # if root == None:
        #     return res
        # if root.val != None:
        #     res.append(root.val)
        # if root.left != None:
        #     res += self.preorderTraversal(root.left)
        # if root.right != None:
        #     res += self.preorderTraversal(root.right)
        #
        # return res