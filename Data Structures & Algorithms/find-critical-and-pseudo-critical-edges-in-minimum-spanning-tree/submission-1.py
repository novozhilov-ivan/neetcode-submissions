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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        for i, e in enumerate(edges):
            e.append(i)  # [n1, n2, weight, original_index]
        
        edges.sort(key=lambda e: e[2])
        mst_weight = 0

        uf = DSU(n)
        for v1, v2, w8, i in edges:
            if uf.union(v1, v2):
                mst_weight += w8
        
        critical, pseudo = [], []
        for n1, n2, e_weight, i in edges:
            weight = 0
            uf = DSU(n)
            for v1, v2, w, j in edges:
                if i != j and uf.union(v1, v2):
                    weight += w
            if max(uf.size) != n or weight > mst_weight:
                critical.append(i)
                continue
            
            # Try with curr edge
            uf = DSU(n)
            uf.union(n1, n2)
            weight = e_weight
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    weight += w
            if weight == mst_weight:
                pseudo.append(i)
        return [critical, pseudo]
        
