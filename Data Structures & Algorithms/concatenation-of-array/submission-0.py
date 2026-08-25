class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [0] * l * 2
        for i in range(l):
            ans[i] = ans[i + l] = nums[i]
        
        return ans