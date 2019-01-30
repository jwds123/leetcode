'''
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树
'''
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1, 2]  # 0个则返回1
        if n <= 2:
            return dp[n]
        else:
            dp += [0] * (n - 2)
            for i in range(3, n + 1):  # 一直到dp[n]
                for j in range(1, i + 1):#count[i]=count[0]*count[i-1]+count[1]*count[i-2]+...+count[i-1]*count[0]
                    #i>=3 i-1>=2
                    dp[i] += dp[j - 1] * dp[i - j]
            return dp[n]
if __name__ == '__main__':
    sol = Solution()
    print(sol.numTrees(4))