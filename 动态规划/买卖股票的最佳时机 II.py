'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        profit = 0
        while i < len(prices) - 1:
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]

            i += 1
        return profit
if __name__ == '__main__':
    l=[7,1,5,3,6,4]
    #(5-1)+(6-3)=(5-1)+(6-3)
    l1=[1,2,6,5,7]
    #(6-1)+(7-5)=(2-1)+(6-2)+(7-5)
    sol = Solution()
    res=sol.maxProfit(l1)
    print(res)