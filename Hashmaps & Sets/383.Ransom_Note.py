# Time O(n + m), Space: O(n)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        appearences = {}
        for char in magazine:
            if char not in appearences:
                appearences[char] = 0
            appearences[char] += 1
        
        for char in ransomNote:
            if char not in appearences or appearences[char] == 0:
                return False
            appearences[char] -= 1
        
        return True