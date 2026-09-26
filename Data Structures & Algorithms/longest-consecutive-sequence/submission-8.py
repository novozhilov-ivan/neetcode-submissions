class UnionFind:
    def __init__(self, n: int) -> None:
        self.par = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, node: int) -> int:
        while node != self.par[node]:
            self.par[node] = self.par[self.par[node]]
            node = self.par[node]
        return node
    
    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.size[p1] > self.size[p2]:
            p1, p2 = p2, p1
        self.size[p1] += self.size[p2]
        self.par[p2] = p1
        return True


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        if not num_set: 
            return 0
        uf = UnionFind(len(nums))

        i_to_num = {num: i for i, num in enumerate(num_set)}

        for num in num_set:
            if num + 1 in num_set:
                uf.union(i_to_num[num], i_to_num[num + 1])
        return max(uf.size)
