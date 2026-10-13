class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)
        if N < M:
            N, M = M, N
            word1, word2 = word2, word1
        
        dp = [0] * (M + 1)
        next_dp = [0] * (M + 1)

        for j in range(M + 1):
            dp[j] = M - j
        
        for i in range(N - 1, -1, -1):
            next_dp[M] = N - i
            for j in range(M - 1, -1, -1):
                if word1[i] == word2[j]:
                    next_dp[j] = dp[j + 1]
                else:
                    next_dp[j] = 1 + min(
                        dp[j],
                        dp[j + 1],
                        next_dp[j + 1],
                    )
            dp = next_dp[:]
        return dp[0]
