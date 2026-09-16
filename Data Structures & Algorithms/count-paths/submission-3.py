class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [0] * m

        for i in range(n - 1, -1, -1):
            curr_row = [0] * m
            curr_row[m - 1] = 1
            for j in range(m - 2, -1, -1):
                curr_row[j] = curr_row[j + 1] + prev_row[j]

            prev_row = curr_row
        
        return prev_row[0]