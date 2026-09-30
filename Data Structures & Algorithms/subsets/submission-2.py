class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub_sets, cur_set = [], []
        nums.sort()
    
        def helper(i, nums, cur_set, sub_sets):
            
            if i >= len(nums):
                sub_sets.append(cur_set.copy())
                return
            
            cur_set.append(nums[i])
            helper(i + 1, nums, cur_set, sub_sets)
            cur_set.pop()
        
        helper(0, nums, cur_set, sub_sets)
        return sub_sets