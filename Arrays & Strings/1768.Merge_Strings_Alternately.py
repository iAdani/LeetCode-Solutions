class Solution:
    # O(N)
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        idx = 0
        while idx < min(len(word1), len(word2)):
            merged += word1[idx] + word2[idx]
            idx += 1
        
        if idx < len(word1):
            merged += word1[idx:]
        if idx < len(word2):
            merged += word2[idx:]
        
        return merged
    
    # O(N)
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        n, m = len(word1), len(word2)
        i = 0
        while i < min(n, m):
            res += word1[i]
            res += word2[i]
            i += 1
        
        while i < n:
            res += word1[i]
            i += 1
        while i < m:
            res += word2[i]
            i += 1
        
        return res
    