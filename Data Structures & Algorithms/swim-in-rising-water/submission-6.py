class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        min_heap = [(grid[0][0], 0, 0)]
        visit.add((0, 0))

        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            if r == N - 1 and c == N - 1:
                return t

            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c

                if (
                    min(nei_r, nei_c) < 0
                    or max(nei_r, nei_c) >= N
                    or (nei_r, nei_c) in visit
                ):
                    continue
                visit.add((nei_r, nei_c))
                heapq.heappush(min_heap, (max(t, grid[nei_r][nei_c]), nei_r, nei_c))
