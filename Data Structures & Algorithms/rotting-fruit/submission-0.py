class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        diffs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        fresh, time = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        

        while q and fresh > 0:

            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in diffs:
                    if (
                        min(r + dr, c + dc) < 0
                        or r + dr >= ROWS
                        or c + dc >= COLS
                        or grid[r + dr][ c + dc] != 1
                    ):
                        continue
                    
                    q.append((r + dr, c + dc))
                    fresh -= 1
                    grid[r + dr][c + dc] = 2
            time += 1
        
        return time if fresh == 0 else -1
