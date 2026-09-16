class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        m, n = len(grid), len(grid[0])
        prev_row = [0] * m
        prev_row[m] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    dp[j] = 0
                else:
                    dp[j] += dp[j + 1]
        
        return dp[0]