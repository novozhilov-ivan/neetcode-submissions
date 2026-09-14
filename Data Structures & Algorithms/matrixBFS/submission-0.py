class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visit = set()

        length = 0
        diffs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue.append((0, 0))
        visit.add((0, 0))
    
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                for dr, dc in diffs:
                    if (
                        min(r + dr, c + dc) < 0
                        or r + dr >= ROWS
                        or c + dc >= COLS
                        or (r + dr, c + dc) in visit
                        or grid[r + dr][c + dc] == 1
                    ):
                        continue
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1
        
        return length