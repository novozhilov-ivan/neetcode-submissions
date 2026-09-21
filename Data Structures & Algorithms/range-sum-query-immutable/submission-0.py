class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        self.total = 0

        for num in nums:
            self.total += num
            self.prefix.append(self.total)

    def sumRange(self, left: int, right: int) -> int:
        pre_right = self.prefix[right]
        pre_left = self.prefix[left - 1] if left else 0
        return pre_right - pre_left  
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)