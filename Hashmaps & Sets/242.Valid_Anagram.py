class Solution:
    # Time: O(n), Space: O(n + m)
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

    # Time: O(n), Space: O(n + m)
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if len(s) != len(t) or set(s) != set(t):
            return False
        
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            freq[t[i]] = freq.get(t[i], 0) - 1
        
        if all(x == 0 for x in freq.values()):
            return True
        return False
    
    # Since s and t consist of lowercase English letters
    # only, the freq can only have O(1) keys, and each 
    # key can only have a maximum of size(int) bits
    # representation. Therefore in that case, the space 
    # complexity is O(1), and in the general case, without
    # the length constraint, it is O(log(N)).