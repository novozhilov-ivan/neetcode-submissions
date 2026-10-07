class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, dst, in edges:
            adj[src].append(dst)
        
        visit = set()
        visiting = set()
        top_sort = []

        def dfs(src):
            if src in visit:
                return True
            if src in visiting:
                return False

            visiting.add(src)
            
            for neighbor in adj[src]:
                if not dfs(neighbor):
                    return False
            visiting.remove(src)
            visit.add(src)
            top_sort.append(src)
            return True

            
        for i in range(n):
            if not dfs(i):
                return []

        top_sort.reverse()
        return top_sort
