class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        length = len(nums)
        shift = 0
        for i in range(length):
            if nums[i] == val:
                shift += 1
                continue
            
            nums[i - shift] = nums[i]
        
        return length - shift
            