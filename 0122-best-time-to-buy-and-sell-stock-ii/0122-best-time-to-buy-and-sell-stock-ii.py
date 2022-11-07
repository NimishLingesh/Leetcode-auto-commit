class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
        """stock_min, max_profit = float('inf'), 0
        for price in prices:
            stock_min = min(stock_min, price)
            max_profit = max(max_profit, price - stock_min)
        return max_profit"""