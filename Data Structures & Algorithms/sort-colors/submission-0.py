class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)

        i = 0
        for n in range(len(count)):
            for j in range(count[n]):
                nums[i] = n
                i += 1
            