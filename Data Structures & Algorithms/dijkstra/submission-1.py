class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for s, dst, w8 in edges:
            adj[s].append((dst, w8))
        
        shortest = {}
        min_heap = [(0, src)]

        while min_heap:
            w1, d1 = heapq.heappop(min_heap)
            if d1 in shortest:
                continue
            shortest[d1] = w1

            for d2, w2 in adj[d1]:
                if d2 not in shortest:
                    heapq.heappush(min_heap, (w1 + w2, d2))
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest
