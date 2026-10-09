class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones_sum = sum(stones)
        target = stones_sum // 2
        dp = {0}

        for stone in stones:
            next_dp = set(dp)
            for val in dp:
                if val + stone == target:
                    return stones_sum - 2 * target
                if val + stone < target:
                    next_dp.add(val + stone)
            dp = next_dp

        return stones_sum - 2 * max(dp)
