class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:      
        return self.helper(0, nums)

    def helper(self, i, nums):
        if i == len(nums):
            return [[]]
        
        res_perms = []
        perms = self.helper(i + 1, nums)
        for p in perms:
            for j in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(j, nums[i])
                res_perms.append(p_copy)
        return res_perms