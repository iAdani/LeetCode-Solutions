class Solution:
    # Time: O(N), Space: O(1)
    def backspaceCompare(self, s: str, t: str) -> bool:

        def getNextValid(i, s):
            back = 0
            while i > -1:
                if s[i] == '#':
                    back += 1
                elif back > 0:
                    back -= 1
                else:
                    return i
                i -= 1
            
            return i


        i, j = len(s) - 1, len(t) - 1
        while i > -1 or j > -1:
            i = getNextValid(i, s)
            j = getNextValid(j, t)

            if i < 0 and j < 0:
                return True
            if i < 0 or j < 0:
                return False
            if s[i] != t[j]:
                return False
            i -= 1
            j -= 1
        
        return True
    