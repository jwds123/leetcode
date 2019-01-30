class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def postorderTraversal(self, root):
        """
        left->right->root
        [[left],[right],root]
        难点在于不知道左右子树是否已经遍历完
        """
        '''
        后序遍历时， 先后序遍历左子树，再后序遍历右子树，最后访问该节点。
        也就是说第一次遍历到一个节点的时候，我们不将其加入到结果中，只有当它的左右子树都遍历完后，我们将该节点加入到结果中。
        
        跟先序遍历中一样，我们也通过栈来解决，把接下去要访问的节点压入栈中。
        
        由于现在每个节点都要遍历两次，我们给节点添加一个标志位，如果一个节点还没有访问过，我们给的标志为visit，
        表示下一次遇到它只是第一次访问它，在访问它之后，我们把它的标志改为get并再次压栈，表示下一次遇到它要访问它的值。
        
        同时还要将它的右子树和左子树分别压栈，表示要后续遍历左子树和右子树。对于第二次访问的节点，将其加入结果中。
        '''
        if not root:
            return []
        res = []
        stack = [(root, 'visit')]
        while stack:
            node, label = stack.pop()
            # 还未遍历过，需要将node加入。入栈顺序：root-right-left,出栈反序
            if label == 'visit':
                # 访问过该节点，同时压入右子树和左子树；
                # [root(get),right(visit),left(visit)] --> [root(get),right(get),left(get),lright(visit),lleft(visit)]
                stack.append((node, 'get'))
                if node.right:
                    stack.append((node.right, 'visit'))
                if node.left:
                    stack.append((node.left, 'visit'))

            # 已经遍历过该点及其左子树与右子树，再将改点加入结果中
            else:
                res.append(node.val)
        return res

