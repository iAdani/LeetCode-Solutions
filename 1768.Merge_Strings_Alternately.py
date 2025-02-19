class Solution:
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
    