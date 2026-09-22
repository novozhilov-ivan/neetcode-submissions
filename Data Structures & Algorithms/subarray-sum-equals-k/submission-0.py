class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        prefix_sum = {0: 1}

        for n in nums:
            cur_sum += n
            diff = cur_sum - n

            count = prefix_sum.get(diff, 0)
            res += count
            prefix_sum[diff] = 1 + count

        return res