class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_max = 0
        temp = 0
        for num in nums:
            if num:
                temp += 1
            else:
                temp = 0
            
            curr_max = max(curr_max, temp)
        
        return curr_max