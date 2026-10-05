class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        visit = set()
        min_h = [[0, 0]]
        res = 0

        while len(visit) < n:
            cost, i = heapq.heappop(min_h)
            if i in visit:
                continue
            res += cost
            visit.add(i)

            for nei_cost, neighbor in adj[i]:
                if neighbor not in visit:
                    heapq.heappush(min_h, [nei_cost, neighbor])

        return res

