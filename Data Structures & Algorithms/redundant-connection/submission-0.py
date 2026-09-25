class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(node: int) -> int:
            if node != par[node]:
                par[node] = find(par[node])
            return par[node]
        
        def union(node1: int, node2: int) -> int:
            p1, p2 = find(node1), find(node2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p1] = p2
                rank[p1] += rank[p2]
            else:
                par[p2] = p1
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
