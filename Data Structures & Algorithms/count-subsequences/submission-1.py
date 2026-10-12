class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        N, M = len(s), len(t)
        cache = [[-1] * (M + 1) for _ in range(N + 1)]

        def dfs(i, j, cache):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            
            cache[i][j] = dfs(i + 1, j, cache)
            if s[i] == t[j]:
                cache[i][j] += dfs(i + 1, j + 1, cache)
            return cache[i][j]

        return dfs(0, 0, cache)
