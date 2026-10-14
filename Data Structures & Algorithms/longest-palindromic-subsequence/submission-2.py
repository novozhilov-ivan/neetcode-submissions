class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[0] * N for _ in range(N)]

        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(
                        dp[i + 1][j],
                        dp[i][j - 1],
                    )
        return dp[0][N - 1]