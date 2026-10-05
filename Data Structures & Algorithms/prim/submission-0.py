class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst, weight in edges:
            adj[src].append([dst, weight])
            adj[dst].append([src, weight])
        
        visit = set()
        min_h = [[0, 0]]
        res = 0

        while min_h and len(visit) < n:
            weight, dst = heapq.heappop(min_h)
            if dst in visit:
                continue
            
            visit.add(dst)
            res += weight

            for neighbor, w8 in adj[dst]:
                if neighbor not in visit:
                    heapq.heappush(min_h, [w8, neighbor])
        
        return res if len(visit) == n else -1
