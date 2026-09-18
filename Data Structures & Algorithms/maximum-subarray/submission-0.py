class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, max_sum = 0, nums[0]

        for num in nums:
            cur_sum = max(cur_sum, 0) + num
            max_sum = max(max_sum, cur_sum)
        
        return max_sum