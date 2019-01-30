'''
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
以 i 为根节点，那么其左子树由[1, i - 1]构成，右子树由[i + 1, n] 构成;
要构建包含1到n的二叉搜索树，只需遍历1到n中的数作为根节点，
以i为界将数列分为左右两部分，小于i的数作为左子树，大于i的数作为右子树，
使用两重循环将左右子树所有可能的组合链接到以i为根节点的节点上;

容易看出，以上求解的思路非常适合用递归来处理，接下来便是设计递归的终止步、输入参数和返回结果了。
由以上分析可以看出递归严重依赖数的区间和i,不妨设『数的区间』两个输入参数分别为start和end.
区间[start,end]也就是构成该子树的元素的范围
如果start>end则表明左右子树均为空
'''
from collections import deque
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        return self.helper(1,n)

    def helper(self,start,end):
        result=[]
        #左右子树为空
        if start>end:
            result.append(None)
            return result
        '''
        i=1 leftTree=None rightTree~[2,n]
        rightTree:leftTree rightTree;  一直到最后一层 结束：没有元素即start>end
        '''
        for i in range(start,end+1):
            leftTree=self.helper(start,i-1)
            rightTree=self.helper(i+1,end)
            for m in range(len(leftTree)):
                for n in range(len(rightTree)):
                    root=TreeNode(i)
                    root.left=leftTree[m]
                    root.right=rightTree[n]
                    result.append(root)

        return result

    def treeNodeToString(self,root):
        if not root:
            return []
        output = []
        queue = [root]
        current = 0
        while current != len(queue):
            #按次序加入queue中的节点
            node = queue[current]

            current = current + 1

            if not node:
                output.append('null')
                continue

            output.append(node.val)
            #依次按照左子树右子树加入queue中
            queue.append(node.left)
            queue.append(node.right)
        return output[:-2]

if __name__ == '__main__':
    sol = Solution()
    res=sol.generateTrees(5)
    for root in res:
        print(sol.treeNodeToString(root))



