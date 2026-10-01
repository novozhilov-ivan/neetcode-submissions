class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combs = []
        kb = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def helper(i, cur_str):
            if len(cur_str) == len(digits):
                combs.append(cur_str)
                return
            
            for c in kb[digits[i]]:
                helper(i + 1, cur_str + c)
        
        if digits:
            helper(0, "")
        return combs