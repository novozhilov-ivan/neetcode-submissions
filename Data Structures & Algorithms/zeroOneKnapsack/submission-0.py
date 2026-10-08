class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return self.dfs(0, capacity, weight, profit)

    def dfs(self, i, capacity, weight, profit):
        if i == len(profit):
            return 0
        
        max_profit = self.dfs(i + 1, capacity, weight, profit)

        new_cap = capacity - weight[i]
        if new_cap >= 0:
            p = profit[i] + self.dfs(i + 1, new_cap, weight, profit)
            max_profit = max(max_profit, p)
        

        return max_profit