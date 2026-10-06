class DSU:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x1: int, x2: int) -> bool:
        root_x, root_y = self.find(x1), self.find(x2)

        if root_x != root_y:
            if self.size[root_x] > self.size[root_y]:
                self.size[root_x] += self.size[root_y]
                self.parent[root_y] = root_x
            else:
                self.size[root_y] += self.size[root_x]
                self.parent[root_x] = root_y
            return True
        return False


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        min_h = []
        for n1, n2, w8 in edges:
            heapq.heappush(min_h, [w8, n1, n2])
        
        uf = DSU(n)
        res, components = 0, n

        while components > 1 and min_h:
            w, n1, n2 = heapq.heappop(min_h)
            if uf.union(n1, n2):
                res += w
                components -= 1            

        return res if components == 1 else -1