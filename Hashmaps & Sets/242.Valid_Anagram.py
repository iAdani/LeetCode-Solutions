# Time: O(n), Space: O(n + m)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if len(s) != len(t) or set(s) != set(t):
            return False
        
        for letter in s:
            if letter not in freq:
                freq[letter] = 0
            freq[letter] += 1
        
        for letter in t:
            if letter not in freq or freq[letter] == 0:
                return False
            freq[letter] -= 1
        
        if all(x == 0 for x in freq.values()):
            return True
        return False