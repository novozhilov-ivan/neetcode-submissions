class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rigth_max = -1

        for i in range(len(arr) - 1, -1, -1):
            new_max = max(arr[i], rigth_max)
            arr[i] = rigth_max
            rigth_max = new_max
        
        return arr
