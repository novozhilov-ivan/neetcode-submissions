class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append((dst, succProb[i]))
            adj[dst].append((src, succProb[i]))
        
        max_h = [(-1, start_node)]
        visit = set()

        while max_h:
            prob, cur = heapq.heappop(max_h)
            visit.add(cur)

            if cur == end_node:
                return -1 * prob

            for dst, prob2 in adj[cur]:
                if dst in visit:
                    continue
                heapq.heappush(max_h, (prob2 * prob, dst))
        
        return 0
