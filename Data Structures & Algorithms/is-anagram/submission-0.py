class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for char_s, char_t in zip(s, t):
            count[ord("a") - ord(char_s)] += 1
            count[ord("a") - ord(char_t)] -= 1
        
        return all(c == 0 for c in count)
