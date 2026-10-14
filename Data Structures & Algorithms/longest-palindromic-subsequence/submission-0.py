class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[-1] * N for _ in range(N)]

        def dfs(i, j):
            if i < 0 or j == N:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i] == s[j]:
                length = 1 if i == j else 2
                dp[i][j] = length + dfs(i - 1, j + 1)
            else:
                dp[i][j] = max(
                    dfs(i - 1, j),
                    dfs(i, j + 1),
                )
            return dp[i][j]
        
        for i in range(N):
            dfs(i, i)
            dfs(i, i + 1)
        
        return max(max(row) for row in dp if row != -1)
        