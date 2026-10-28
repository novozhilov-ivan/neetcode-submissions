class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

    def lcp(self, word: str, prefix_len: int) -> int:
        node = self.root
        for i in range(min(len(word), prefix_len)):
            if word[i] not in node.children:
                return i
            node = node.children[word[i]]
        return min(len(word), prefix_len)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        mini = 0
        for i in range(1, len(strs)):
            if len(strs[mini]) > len(strs[i]):
                mini = i
        
        trie = Trie()
        trie.insert(strs[mini])
        prefix_len = len(strs[mini])
        for i in range(len(strs)):
            prefix_len = trie.lcp(strs[i], prefix_len)

        return strs[0][:prefix_len]


