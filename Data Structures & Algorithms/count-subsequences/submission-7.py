class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N, M = len(s), len(t)
        dp = [1] + [0] * M


        for i in range(N):
            cur_row = [1] + [0] * M
            for j in range(1 , M + 1):
                cur_row[j] = dp[j]
                if s[i] == t[j - 1]:
                    cur_row[j] += dp[j - 1]
            dp = cur_row
        return dp[M]
