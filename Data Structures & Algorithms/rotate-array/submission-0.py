class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = k - 1, len(nums) - 1

        while k:
            nums[l], nums[r] = nums[r], nums[l]
            k -= 1
            l -= 1
            r -= 1
        