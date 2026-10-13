class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N, M = len(s), len(t)
        dp = [0] * (M + 1)
        dp[-1] = 1

        for i in range(N - 1, -1, -1):
            next_dp = [0] * (M + 1)
            next_dp[-1] = 1
            for j in range(M - 1, -1, -1):
                next_dp[j] = dp[j]
                if s[i] == t[j]:
                    next_dp[j] += dp[j + 1]
            dp = next_dp
        return dp[0]
