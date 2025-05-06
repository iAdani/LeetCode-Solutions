class Solution:
    # O(N)
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return isPalindrome(start + 1, end) or isPalindrome(start, end - 1)
            start += 1
            end -= 1
        
        return True
    
    # O(N)
    # Not mine but I LOVE it and want to keep it
    # It works because slicing does not include the second index, 
    # so automatically right one will be removed, and then the left
    # one is removed
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return s[start:end] == s[start:end][::-1] or s[start+1:end+1] == s[start+1:end+1][::-1]
            start += 1
            end -= 1
        
        return True