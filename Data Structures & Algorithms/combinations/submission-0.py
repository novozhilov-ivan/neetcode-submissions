class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        self.helper(1, [], combs, n, k)
        return combs
    
    def helper(self, i, cur_comb, combs, n, k):
        if len(cur_comb) == k:
            combs.append(cur_comb.copy())
            return
        
        if i > n:
            return
        
        for j in range(i, n + 1):
            cur_comb.append(j)
            self.helper(j + 1, cur_comb, combs, n, k)
            cur_comb.pop()
        