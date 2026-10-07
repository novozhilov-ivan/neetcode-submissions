class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[crs].append(pre)

        def dfs(crs):
            if crs not in prereq_map:
                prereq_map[crs] = set()
                for pre in adj[crs]:
                    prereq_map[crs] |= dfs(pre)
                prereq_map[crs].add(crs)
            return prereq_map[crs]

        prereq_map: dict[int, set[int]] = {}
        for crs in range(numCourses):
            dfs(crs)
        
        res = []
        for u, v in queries:
            res.append(u in prereq_map[v])
        return res
