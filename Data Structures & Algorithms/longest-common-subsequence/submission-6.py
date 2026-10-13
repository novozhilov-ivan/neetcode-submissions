class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)
        dp = [0] * (M + 1)

        for i in range(N):
            next_dp = [0] * (M + 1)
            for j in range(M):
                if text1[i] == text2[j]:
                    next_dp[j + 1] = 1 + dp[j]
                else:
                    next_dp[j + 1] = max(
                        dp[j + 1],
                        next_dp[j],
                    )
            dp = next_dp
        return dp[M]
