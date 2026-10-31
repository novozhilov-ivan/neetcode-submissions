class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        l, r = 0, len(s) - 1
        one_miss = False

        while l < r:
            if s[l] == s[r]:
                r -= 1
                l += 1
                continue

            if one_miss:
                return False
            l += 1     
        
        return True
