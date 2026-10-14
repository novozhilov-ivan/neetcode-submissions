class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_idx, res_len = 0, 0
        N = len(s)
        dp = [False] * N

        for i in range(N - 1, -1, -1):
            next_dp = [False] * N
            for j in range(i, N):
                if (
                    s[i] == s[j]
                    and (j - i <= 2 or dp[j - 1])
                ):
                    next_dp[j] = True
                    if res_len < (j - i + 1):
                        res_idx = i
                        res_len = j - i + 1
            dp = next_dp
        return s[res_idx : res_idx + res_len]
