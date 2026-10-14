class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        res = 0
        dp = [[False] * N for _ in range(N)]

        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1

        return res
