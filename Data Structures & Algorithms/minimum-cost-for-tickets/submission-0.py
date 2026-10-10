class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (len(days) + 1)

        for i in reversed(range(len(days))):
            j = i
            dp[i] = float("inf")
            for cost, durations in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < days[i] + durations:
                    j += 1
                dp[i] = min(dp[i], cost + dp[j])
        return dp[0]
