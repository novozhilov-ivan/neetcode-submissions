class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        target = image[sr][sc]
        def dfs(image, r, c, visit):
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit
                or image[r][c] != target
            ):
                return
            image[r][c] = color
            visit.add((r, c))
            dfs(image, r + 1, c, visit)
            dfs(image, r - 1, c, visit)
            dfs(image, r, c + 1, visit)
            dfs(image, r, c - 1, visit)    
            visit.remove((r, c))    

        dfs(image, sr, sc, set())
        return image