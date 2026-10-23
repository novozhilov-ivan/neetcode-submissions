class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("-inf")
        sell, cooldown = 0, 0

        for price in prices:
            next_buy = max(buy, cooldown - price)
            next_sell = buy + price
            cooldown = max(cooldown, sell)

            buy, sell = next_buy, next_sell
        
        return max(sell, cooldown)
