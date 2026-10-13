class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N, M = len(s1), len(s2)
        if N + M != len(s3):
            return False
        
        if N < M:
            N, M = M, N
            s1, s2 = s2, s1

        dp = [False] * (M + 1)
        dp[M] = True

        for i in range(N, -1, -1):
            next_dp = [False] * (M + 1)
            if i == N:
                next_dp[M] = True
            for j in range(M, -1, -1):
                if i < N and s1[i] == s3[i + j] and dp[j]:
                    next_dp[j] = True
                if j < M and s2[j] == s3[i + j] and next_dp[j + 1]:
                    next_dp[j] = True
            dp = next_dp
        return dp[0]