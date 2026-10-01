class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
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
        digits = "".join(sorted(digits))
        letters = "".join([kb[digit] for digit in digits])

        def helper(i, cur_letters):
            if len(cur_letters) == len(digits):
                combs.append(cur_letters)
                return
            if len(cur_letters) >= len(digits):
                return
            
            for j in range(i + 1, len(letters)):
                helper(j, cur_letters + letters[j])
            
        helper(0, "")
        return combs