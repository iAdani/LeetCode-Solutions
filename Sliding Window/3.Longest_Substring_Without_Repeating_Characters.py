class Solution:
    # O(N)
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        l = r = 0
        while r < len(s):
            ch = s[r]
            while ch in s[l:r]:
                l += 1
            
            r += 1
            maxi = max(maxi, r - l)
        
        return maxi
