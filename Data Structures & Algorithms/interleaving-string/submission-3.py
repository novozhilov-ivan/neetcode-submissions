class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N, M = len(s1), len(s2)
        if N + M != len(s3):
            return False
        dp = [[False] * (M + 1) for _ in range(N + 1)]

        dp[N][M] = True

        for i in range(N, -1, -1):
            for j in range(M, -1, -1):
                if i < N and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < M and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
                
        return dp[0][0]