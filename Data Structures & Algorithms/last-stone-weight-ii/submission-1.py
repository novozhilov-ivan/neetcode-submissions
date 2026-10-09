class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones_sum = sum(stones)
        target = stones_sum // 2
        dp = [0] * (target + 1)

        for stone in stones:
            for t in range(target, stone - 1, -1):
                dp[t] = max(
                    dp[t],
                    stone + dp[t - stone],
                )

        return stones_sum - 2 * dp[target]
