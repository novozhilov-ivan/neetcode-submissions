class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [0] * N

        for i in range(N - 1, -1, -1):
            next_dp = [0] * N
            next_dp[i] = 1
            for j in range(i + 1, N):
                if s[i] == s[j]:
                    next_dp[j] = 2 + dp[j - 1]
                else:
                    next_dp[j] = max(
                        dp[j],
                        next_dp[j - 1],
                    )
            dp = next_dp
        return dp[N - 1]