class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        N, M = len(str1), len(str2)
        dp = [str2[j:] for j in range(M)] + [""]

        for i in reversed(range(N)):
            next_dp = [""] * M + [str1[i:]]
            for j in reversed(range(M)):
                if str1[i] == str2[j]:
                    next_dp[j] = str1[i] + dp[j + 1]
                else:
                    res1 = str1[i] + dp[j]
                    res2 = str2[j] + next_dp[j + 1]
                    next_dp[j] = res1 if len(res1) < len(res2) else res2
            dp = next_dp
        
        return dp[0]
