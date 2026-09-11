class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if (second_num := target - num) in seen:
                return [min(i, seen[second_num]), max(i, seen[second_num])]
            seen[num] = i
        
        