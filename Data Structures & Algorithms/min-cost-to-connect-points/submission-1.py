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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        
        edges.sort()
        res = 0

        for dist, n1, n2 in edges:
            if dsu.union(n1, n2):
                res += dist

        return res

