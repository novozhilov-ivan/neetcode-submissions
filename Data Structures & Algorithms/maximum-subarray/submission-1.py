class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, max_sum = 0, nums[0]

        for num in nums:
            cur_sum, max_sum = max(cur_sum + num, num), max(max_sum, max(cur_sum + num, num))
        
        return max_sum