class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, r = 0, mountainArr.length() - 1

        while l <= r:
            m = l + (r - l) // 2
            if mountainArr.get(m) < target:
                l = m + 1
            elif mountainArr.get(m) > target:
                r = m - 1
            else:
                return m
        return -1
