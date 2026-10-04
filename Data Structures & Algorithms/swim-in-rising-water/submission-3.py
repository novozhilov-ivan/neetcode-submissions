class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        neighbors = defaultdict(list)
        for i in range(N):
            for j in range(N):
                if i + 1 < N:
                    neighbors[(i, j)].append((i + 1, j))
                if j + 1 < N:
                    neighbors[(i, j)].append((i, j + 1))
                if i - 1 > N:
                    neighbors[(i, j)].append((i - 1, j))
                if j - 1 > N:
                    neighbors[(i, j)].append((i, j - 1))

        visit = set()
        min_heap = [(grid[0][0], 0, 0)]
        visit.add((0, 0))

        while min_heap:
            t, i, j = heapq.heappop(min_heap)
            if i == N - 1 and j == N - 1:
                return t

            for nei_r, nei_c in neighbors[(i, j)]:
                if (nei_r, nei_c) in visit:
                    continue
                visit.add((nei_r, nei_c))
                heapq.heappush(min_heap, (max(t, grid[nei_r][nei_c]), nei_r, nei_c))

        return t
