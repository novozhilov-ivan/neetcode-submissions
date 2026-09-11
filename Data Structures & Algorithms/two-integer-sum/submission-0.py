class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            if hm.get(target - nums[i]) is not None:
                first, second = hm[target - nums[i]], i
                return [min(first, second), max(first, second)]
            hm[nums[i]] = i
        
        