class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[crs].append(pre)

        
        prereq_map = {}
        for crs in range(numCourses):
            dfs(crs)
        
        res = []
        for u, v in queries:
            res.append(u in prereq_map[v])
