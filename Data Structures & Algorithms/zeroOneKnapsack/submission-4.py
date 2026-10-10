class Solution:
    def maximumProfit(self, profit, weight, capacity):
        N, M = len(profit), capacity
        dp = [0] * (M + 1)

        # Fill the first row to reduce edge cases
        for c in range(M + 1):
            if weight[0] <= c:
                dp[c] = profit[0] 

        for i in range(1, N):
            curRow = [0] * (M + 1)
            for c in range(1, M + 1):
                skip = dp[c]
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + dp[c - weight[i]]
                curRow[c] = max(include, skip)
            dp = curRow
        return dp[M]