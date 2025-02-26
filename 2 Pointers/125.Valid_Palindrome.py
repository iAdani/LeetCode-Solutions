# O(N)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())        
        start, end = 0, len(s) - 1
        while start <= end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True