class Solution:
    # O(N)
    def firstUniqChar(self, s: str) -> int:
        freqs = [0] * 26
        for c in s:
            freqs[ord(c) - ord('a')] += 1
        
        for idx, c in enumerate(s):
            if freqs[ord(c) - ord('a')] == 1:
                return idx

        return -1