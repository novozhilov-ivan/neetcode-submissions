class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        res = cur_sum = 0

        for R in range(len(arr)):
            cur_sum += arr[R]
            if R >= k - 1:
                res += cur_sum >= threshold
                cur_sum -= arr[R - k + 1]
        return res
        