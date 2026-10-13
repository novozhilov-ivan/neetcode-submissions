class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)

        def dfs(i, j):
            if i == N:
                return M - j
            if j == M:
                return N - i
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            res = min(
                dfs(i + 1, j),
                dfs(i, j + 1),
                dfs(i + 1, j + 1),
            )
            return res + 1

        return dfs(0, 0)
