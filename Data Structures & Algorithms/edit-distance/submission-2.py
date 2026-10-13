class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)
        cache = {}
        
        dp = [[float("inf")] * (M + 1) for _ in range(N + 1)]

        for j in range(M + 1):
            dp[N][j] = M - j
        for i in range(N + 1):
            dp[i][M] = N - i
        
        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i + 1][j],
                        dp[i][j + 1],
                        dp[i + 1][j + 1],
                    )
        return dp[0][0]
