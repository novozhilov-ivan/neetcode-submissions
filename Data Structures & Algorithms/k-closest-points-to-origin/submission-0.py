class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            min_heap.append([dist, x, y])
        
        res = []
        heapq.heapify(min_heap)
        while k > 0:
            _, x, y = heapq.heappop(min_heap)
            res.append([x, y])
            k -= 1
        
        return res

