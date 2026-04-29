class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy_day, sell_day = 0, 0
        max_profit = 0
        for sell_day in range(len(prices)):
            if prices[sell_day] - prices[buy_day] > max_profit:
                max_profit = max(prices[sell_day] - prices[buy_day], max_profit)
            if prices[sell_day] < prices[buy_day]:
                buy_day = sell_day
        return max_profit

        