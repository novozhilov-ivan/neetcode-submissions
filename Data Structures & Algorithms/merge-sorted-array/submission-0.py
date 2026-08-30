class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        L = nums1[:m]
        R = nums2

        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                nums1[k] = L[i]
                i += 1
            else:
                nums1[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            nums1[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            nums1[k] = R[j]
            j += 1
            k += 1
        