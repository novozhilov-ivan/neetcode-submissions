class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        m, n = len(grid), len(grid[0])
        prev_row = [0] * m
        prev_row[m - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    prev_row[j] = 0
                else:
                    prev_row[j] += prev_row[j + 1]
        
        return prev_row[0]