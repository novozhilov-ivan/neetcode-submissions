class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            is_match = (
                i < len(s)
                and (
                    s[i] == p[j]
                    or p[j] == "."
                )
            )
            if j + 1 < len(p) and p[j + 1] == "*":
                dp[(i, j)] = (
                    dfs(i, j + 2)  # dont use "*"
                    or (           # use "*"
                        is_match
                        and dfs(i + 1, j)
                    )
                )
                return dp[(i, j)]

            if is_match:
                return dfs(i + 1, j + 1)
            
            return False        

        return dfs(0, 0)
