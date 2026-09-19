class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = total = 0
        length = float("inf")

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                length = min(length, R - L + 1)
                total -= nums[L]
                L += 1
        return 0 if length == float("inf") else length
