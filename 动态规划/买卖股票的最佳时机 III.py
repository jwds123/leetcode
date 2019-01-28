'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
'''
import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        first_buy, first_sell, second_buy, second_sell = -sys.maxsize, 0, -sys.maxsize, 0
        #print(sys.maxsize)
        for price in prices:
            first_buy = max(first_buy, -price)  # 该天是第一次买入的最大收益
            first_sell = max(first_sell, price + first_buy)  # 在该天第一次卖出的最大收益
            second_buy = max(second_buy, first_sell - price)  # 该天属于第二次买入的最大收益：
            second_sell = max(second_sell, price + second_buy)  # 第二次卖出手上的股票
            #print(price,first_buy,first_sell,second_buy,second_sell)
        return second_sell


        # if not prices or len(prices) == 1:
        #     return 0
        # 
        # profit = []
        # i=buy=0
        # while i <len(prices) -1:
        #     #print(i)
        #     margin = 0
        #     j=i+1
        #     while j<=len(prices)-1 :
        #         if prices[j]>prices[j-1] and j<=len(prices)-1:
        #             #print(prices[j])
        #             margin+=prices[j]-prices[j-1]
        #             j+=1
        # 
        #         else:
        #             buy=j
        #             break
        #     i=buy
        #     profit.append(margin)
        # print(profit)
        # profit.sort(reverse=True)
        # 
        # return profit[0]+profit[1]
if __name__ == '__main__':
    l=[7,1,5,3,6,4]
    #(5-1)+(6-3)=(5-1)+(6-3)
    l1=[3,3,5,0,0,3,1,4]
    #(6-1)+(7-5)=(2-1)+(6-2)+(7-5)
    sol = Solution()
    res=sol.maxProfit(l1)
    print(res)