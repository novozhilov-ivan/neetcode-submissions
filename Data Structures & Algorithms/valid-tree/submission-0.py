class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True
        tree = {i:[] for i in range(n)}

        for node1, node2 in edges:
            tree[node1].append(node2)
            tree[node2].append(node1)

        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for j in tree[i]:
                if j == prev:
                    continue
                
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)
