'''
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        k=len(prices)
        if k<=1:
            return 0
        buy,sell,frozen=[0]*k,[0]*k,[0]*k
        buy[0]=-prices[0]
        for i in range(1,k):
            frozen[i]=sell[i-1]#假设该天是冷冻期，前一天卖了，第二天才是冻结的
            buy[i]=max(buy[i-1],sell[i-2]-prices[i])#假设该天买，那么该天不可以是冷冻期，所以之前累积的收益不是i-1而是i-2天的收益
            sell[i]=max(sell[i-1],buy[i-1]+prices[i])#假设该天卖，没有改变
        return max(sell[-1],frozen[-1])

if __name__ == '__main__':
    l = []
    # (5-1)+(6-3)=(5-1)+(6-3)
    l1 = [1,2,3,0,2]
    # (6-1)+(7-5)=(2-1)+(6-2)+(7-5)
    sol = Solution()
    res = sol.maxProfit(l)
    print(res)