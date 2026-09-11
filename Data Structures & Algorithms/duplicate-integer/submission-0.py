class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1
        
        return bool(next((1 for val in hm.values() if val > 1), False))