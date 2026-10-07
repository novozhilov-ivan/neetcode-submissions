class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for r1, r2 in prerequisites:
            adj[r1].append(r2)
        
        visited, visiting = set(), set()
        
        def dfs(course):
            if course in visited:
                return True
            if course in visiting:
                return False
            
            visiting.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
