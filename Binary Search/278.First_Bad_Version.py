# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # O(log(N))
    def firstBadVersion(self, n: int) -> int:
        r, l = n, 1
        while r > l:
            m = r + ((l - r) // 2)
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        
        return l
        