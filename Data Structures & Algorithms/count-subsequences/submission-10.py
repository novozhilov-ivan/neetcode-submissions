class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N, M = len(s), len(t)
        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for i in range(N + 1):
            dp[i][M] = 1

        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
        return dp[0][0]
