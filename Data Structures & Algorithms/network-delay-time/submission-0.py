class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((t, v))
        
        min_heap = [(0, k)]
        visit = set()
        t = 0

        while min_heap:
            t1, d1 = heapq.heappop(min_heap)
            if d1 in visit:
                continue
            visit.add(d1)
            t = t1

            for t2, d2 in adj[d1]:
                if d2 not in visit:
                    heapq.heappush(min_heap, (t1 + t2, d2))

        return t if len(visit) == n else -1
