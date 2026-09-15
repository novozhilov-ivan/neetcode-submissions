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
        return self.dfs(src, dst, visit)
    
    def dfs(self, src: int, dst: int, visit: set[int]) -> bool:
        if src == dst:
            return True
        visit.add(src)
        for neighbor in self.adj.get(src, set()):
            if neighbor not in visit:
                self.dfs(neighbor, dst, visit)
                return True
        return False

