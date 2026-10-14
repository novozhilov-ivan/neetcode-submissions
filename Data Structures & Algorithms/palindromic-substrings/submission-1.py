class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        res = 0
        dp = [False] * N

        for i in range(N - 1, -1, -1):
            next_dp = [False] * N
            for j in range(i, N):
                if s[i] == s[j] and (j - i <= 2 or dp[j - 1]):
                    next_dp[j] = True
                    res += 1
            dp = next_dp
        return res
