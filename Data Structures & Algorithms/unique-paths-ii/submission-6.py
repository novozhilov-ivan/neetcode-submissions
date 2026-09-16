class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        prev_row = [0] * n
        prev_row[-1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j]:
                    prev_row[j] = 0
                elif j + 1 < n:
                    prev_row[j] += prev_row[j + 1]
        
        return prev_row[0]