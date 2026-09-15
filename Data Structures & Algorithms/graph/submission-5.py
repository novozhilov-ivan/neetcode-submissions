class Graph:
    
    def __init__(self):
        self.adj: dict[int, set[int]] = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj:
            self.adj[src] = set()
        if src not in self.adj:
            self.adj[dst] = set()
        self.adj[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj or dst not in self.adj[src]:
            return False
        self.adj[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        q = deque([src])

        while q:
            curr = q.popleft()
            if curr == dst:
                return True

            visit.add(curr)
            for node in self.adj.get(curr, []):
                if node not in visit:
                    q.append(node)
                    visit.add(node)
        return False
            


