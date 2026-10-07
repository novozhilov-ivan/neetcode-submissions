class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for r1, r2 in prerequisites:
            adj[r1].append(r2)
        
        visiting = set()
        
        def dfs(course):
            if course in visiting:
                return False
            if adj[course] == []:
                return True

            visiting.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
