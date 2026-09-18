class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        glob_max, glob_min = nums[0], nums[0]
        cur_max, cur_min = 0, 0
        total = 0

        for n in nums:
            cur_max = max(cur_max + n, n)
            cur_min = min(cur_min + n, n)
            total += n
            glob_max = max(cur_max, glob_max)
            glob_min = min(cur_min, glob_min)
        
        return max(glob_max, total - glob_min) if glob_max > 0 else glob_max