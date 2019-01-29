'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''
class Solution(object):
    def climbStairs(self, n):
        '''
        f(n) = f(n-1) + f(n-2)
        当n>=3的时候，有两种攀爬方案（即最优子结构的描述）：
        一种是攀登到第n-2层台阶，之后一下迈两个台阶到达n；
        另外一种是攀登到n-1层台阶，然后走一步到达台阶n。
        '''
        if n==1:
            return 1
        elif n==2:
            return 2
        n1,n2=1,1
        for i in range(1,n):
            n1,n2=n2,n1+n2
        return n2

    #递归：超时
    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            n1=self.climbStairs1(n-1)#一次爬一步
            n2=self.climbStairs1(n-2)#一次爬两步
            return n1+n2

if __name__ == '__main__':
    sol = Solution()
    res=sol.climbStairs(5)
    print(res)