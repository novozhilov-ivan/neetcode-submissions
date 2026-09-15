import itertools
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = deque([(0, 0, 1)])
        visit = set((0, 0))
        diffs = [
            [1, -1], [1, 0], [1, 1],
            [0, -1], [0, 1],
            [-1, -1], [-1, 0], [-1, 1],
        ]
        while queue:
            n, m, cur_path = queue.popleft()
            if (
                min(n, m) < 0
                or max(n, m) >= N
                or grid[n][m] == 1
            ):
                continue
            if n == N - 1 and m == N - 1:
                return cur_path
            for dn, dm in diffs:
                if (n + dn, m + dm) not in visit:
                    visit.add((n + dn, m + dm))
                    queue.append((n + dn, m + dm, cur_path + 1))
                    
        return -1
            