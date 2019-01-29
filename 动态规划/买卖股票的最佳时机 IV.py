'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
'''
import sys
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1 or k <= 0:
            return 0
        profit=0
        #如果天数小于2*k+1的话，交易次数必然小于k,选择使得利润最大的交易次数：方法2
        if len(prices)<=2*k+1:
            for i in range(1,len(prices)):
                if prices[i]>prices[i-1]:
                    profit+=prices[i]-prices[i-1]
            return profit
        buy, sell = [-sys.maxsize] * k, [0] * k
        for price in prices:
            for i in range(k):
                buy[i] = max(buy[i], -price) if i == 0 else max(buy[i], sell[i - 1] - price)
                sell[i] = max(sell[i], price + buy[i])
        return sell[-1]
        # first_buy, first_sell, second_buy, second_sell = -sys.maxsize, 0, -sys.maxsize, 0
        # # print(sys.maxsize)
        # for price in prices:
        #     first_buy = max(first_buy, -price)  # 该天属于第一次买入所实现的最大收益
        #     first_sell = max(first_sell, price + first_buy)  # 该天属于第一次卖出所实现的最大收益
        #     second_buy = max(second_buy, first_sell - price)  # 该天属于第二次买入，所实现的最大收益：
        #     second_sell = max(second_sell, price + second_buy)  # 该天属于第二次卖出所实现的最大收益
        #     # print(price,first_buy,first_sell,second_buy,second_sell)
        # return second_sell
if __name__ == '__main__':
    l=[7,1,5,3,6,4]
    #(5-1)+(6-3)=(5-1)+(6-3)
    l1=[3,2,6,5,0,3]
    #(6-1)+(7-5)=(2-1)+(6-2)+(7-5)
    sol = Solution()
    res=sol.maxProfit(2,l1)
    print(res)
