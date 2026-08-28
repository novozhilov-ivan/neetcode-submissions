class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = Counter(students)

        for sandwich in sandwiches:
            if cnt[sandwich] > 0:
                res -= 1
                cnt[sandwich] -= 1
            else:
                break
        return res
