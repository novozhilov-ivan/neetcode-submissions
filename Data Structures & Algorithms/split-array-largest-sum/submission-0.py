class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r


        def can_split(largest):
            sub_array, cur_sum = 0, 0
            
            for n in nums:
                cur_sum += n
                if cur_sum > largest:
                    sub_array += 1
                    cur_sum = n
            return sub_array + 1 <= k


        while l <= r:
            mid = l + (r - l) // 2
            if can_split(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
