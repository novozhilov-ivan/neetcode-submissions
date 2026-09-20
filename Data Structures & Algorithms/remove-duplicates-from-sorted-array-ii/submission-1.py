class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for num in nums:
            if l < 2 or nums != nums[l - 2]:
                nums[l] = nums
                l += 1
        
        return l
