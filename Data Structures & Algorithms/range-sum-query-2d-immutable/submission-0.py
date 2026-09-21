class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])

        self.sum_mat = [
            [0] * (COLS + 1)
            for _ in range(ROWS + 1)
        ]
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sum_mat[r][c + 1]
                self.sum_mat[r + 1][c + 1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1 = row1 + 1
        c1 = col1 + 1
        r2 = row2 + 1
        c2 = col2 + 1

        bottom_right = self.sum_mat[r2][c2]
        bottom_left = self.sum_mat[r2][c1 - 1]
        top_right = self.sum_mat[r1 - 1][c2]
        top_left = self.sum_mat[r1 - 1][c1 - 1]
        return bottom_right + top_left - bottom_left - top_right






# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)