class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) >= 1:
            pBuy = prices[0]
            profit = 0
            for i in prices:
                if i < pBuy:
                    pBuy = i
                else:
                    if i - pBuy > profit:
                        profit = i - pBuy
            return profit
        return 0

Solution.maxProfit(None, [7,1,5,3,6,4])