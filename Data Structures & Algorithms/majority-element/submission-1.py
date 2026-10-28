class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter(nums)
        for num in counter:
            if counter[num] > n // 2:
                return num
