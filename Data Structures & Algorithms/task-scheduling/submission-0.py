class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_h = [-cnt for cnt in count.values()]
        heapq.heapify(max_h)

        time = 0
        q = deque() # pairs [-cnt, idle_time]

        while max_h or q:
            time += 1

            if max_h:
                cnt = 1 + heapq.heappop(max_h)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(max_h, q.popleft()[0])
        
        return time
