class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
        res = []
        stack = ["JFK"]

        while stack:
            while adj[stack[-1]]:
                stack.append(adj[stack[-1]].pop())
            res.append(stack.pop())
        return res[::-1]
