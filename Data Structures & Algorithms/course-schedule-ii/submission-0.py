class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for p1, p2 in prerequisites:
            adj[p1].append(p2)
        
        visit, visiting = set(), set()
        top_sort = []

        def dfs(crs):
            if crs in visit:
                return True
            if crs in visiting:
                return False
            
            visiting.add(crs)

            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            visit.add(crs)
            top_sort.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return top_sort
