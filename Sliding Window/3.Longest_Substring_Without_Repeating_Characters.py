class Solution:
    # O(n^2)
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
    

    # O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n

        subset = set()
        start = end = max_sub = 0
        while end < n:
            if s[end] in subset:
                subset.discard(s[start])
                start += 1
            else:
                subset.add(s[end])
                end += 1
                max_sub = max(max_sub, len(subset))
        
        return max_sub
