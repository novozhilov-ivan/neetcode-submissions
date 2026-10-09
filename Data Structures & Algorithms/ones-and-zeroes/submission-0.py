class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}

        def dfs(i, m, n):
            if i == len(strs):
                return 0
            if (i, m, n) in dp:
                return dp[(i, m, n)]
            
            m_cnt, n_cnt = strs[i].count("0"), strs[i].count("1")
            dp[(i, m, n)] = dfs(i + 1, m, n)
            if m_cnt <= m and n_cnt <= n:
                dp[(i, m, n)] = max(
                    dp[(i, m, n)],
                    1 + dfs(i + 1, m - m_cnt, n - n_cnt),
                )
            return dp[(i, m, n)]
        
        return dfs(0, m, n)