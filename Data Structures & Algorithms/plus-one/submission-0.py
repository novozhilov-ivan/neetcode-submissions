class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s_digits = "".join([str(d) for d in digits])
        int_digits = int(s_digits) + 1
        s_digits = str(int_digits)
        return [c for c in s_digits]
