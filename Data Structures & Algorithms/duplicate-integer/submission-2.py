class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mask = 0
        for num in nums:
            bit = 1 << num
            if mask & bit:
                return True
            mask |= bit
        return False
