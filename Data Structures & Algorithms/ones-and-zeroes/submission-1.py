class Solution:
    def findMaxForm(self, strs: List[str], M: int, N: int) -> int:
        dp = defaultdict(int)

        for i in range(len(strs)):
            s = strs[i]
            m_cnt, n_cnt = strs[i].count("0"), strs[i].count("1")
            for m in range(0, M + 1):
                for n in range(0, N + 1):
                    if m_cnt <= m and n_cnt <= n:
                        dp[(i, m, n)] = max(
                            dp[(i - 1, m, n)],
                            1 + dp[(i - 1, m - m_cnt, n - n_cnt)],
                        )
                    else:
                        dp[(i, m, n)] = dp[(i - 1, m, n)]
        return dp[(len(strs) - 1, M, N)]
