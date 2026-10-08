class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        cache = [[-1] * (M + 1) for _ in range(N)]
        return self.dfs(0, capacity, weight, profit, cache)

    def dfs(self, i, capacity, weight, profit, cache):
        if i == len(profit):
            return 0
        if cache[i][capacity] != -1:
            return cache[i][capacity]

        max_profit = self.dfs(i + 1, capacity, weight, profit, cache)

        new_cap = capacity - weight[i]
        if new_cap >= 0:
            p = profit[i] + self.dfs(i + 1, new_cap, weight, profit, cache)
            max_profit = max(max_profit, p)
        
        cache[i][capacity] = max_profit
        return max_profit