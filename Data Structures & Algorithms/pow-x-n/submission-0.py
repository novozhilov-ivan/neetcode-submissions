class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        temp_n = abs(n)
        res = 1
        while temp_n:
            res *= x
            temp_n -= 1
        return res if n > 0 else 1 / res
