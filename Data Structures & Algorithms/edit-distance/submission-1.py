class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)
        cache = {}
        def dfs(i, j):
            if i == N:
                return M - j
            if j == M:
                return N - i
            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            if (i, j) in cache:
                return cache[(i, j)]
            res = min(
                dfs(i + 1, j),
                dfs(i, j + 1),
                dfs(i + 1, j + 1),
            )
            cache[(i, j)] = res + 1
            return cache[(i, j)]

        return dfs(0, 0)
