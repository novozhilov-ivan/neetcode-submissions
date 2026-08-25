class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        ans = [0] * length
        rigth_max = -1

        for i in range(length - 1, -1, -1):
            ans[i] = rigth_max
            rigth_max = max(rigth_max, arr[i])
        
        return arr
