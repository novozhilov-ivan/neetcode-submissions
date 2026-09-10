class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)

            if x == y:
                continue
            if x < y:
                heapq.heappush(stones, y - x)

        return stones[0]            
