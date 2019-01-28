'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。
输入: [7,1,5,3,6,4]
输出: 5
输入: [7,6,4,3,1]
输出: 0
'''

class Solution(object):
    def maxProfit(self, prices):
        if len(prices)<2:
            return 0
        profit=0
        min_price=prices[0]
        for next_price in prices:
            min_price=min(min_price,next_price)#先记录此前最低的价格
            profit=max(profit,next_price-min_price)#用当前价格减去最低价格
        return profit

    #超出时间限制
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        price_dict={}
        profit=[]
        for i in range(len(prices)-1):
            price_dict[i]=prices[i+1:]
        #print(price_dict)

        for key,value in price_dict.items():
            profit.append(max(value)-prices[key])
        #print(profit)
            return max(max(profit), 0)

if __name__ == '__main__':
    l=[7,1,5,3,6,4]
    sol = Solution()
    res=sol.maxProfit1(l)
    print(res)