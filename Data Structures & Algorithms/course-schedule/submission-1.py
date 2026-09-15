class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return False
        schedule = {}

        for prerequisite in prerequisites:
            course_1, course_2 = prerequisite
            if course_1 not in schedule:
                schedule[course_1] = []
            if course_2 not in schedule:
                schedule[course_2] = []
            schedule[course_1].append(course_2)
        
        finished = set()
        q = deque(list(schedule.keys()))

        while q and numCourses >= 0:
            cour = q.popleft()

            next_courses = schedule[cour]
            if next_courses == [] and numCourses >= 0:
                return True
            
            for c in next_courses:
                q.append(c)

            numCourses -= 1
        
        return False



