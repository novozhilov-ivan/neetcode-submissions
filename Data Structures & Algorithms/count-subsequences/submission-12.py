class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N, M = len(s), len(t)
        dp = [0] * (M + 1)
        dp[0] = 1

        for i in range(1, N + 1):
            next_dp = [0] * (M + 1)
            next_dp[0] = 1
            for j in range(1, M + 1):
                next_dp[j] = dp[j]
                if s[i - 1] == t[j - 1]:
                    next_dp[j] += dp[j - 1]
            dp = next_dp
        return dp[M]
