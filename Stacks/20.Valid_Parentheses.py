# O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in "([{":
                stk.append(c)
            elif not stk or (c == ')' and stk[-1] != '(') \
                        or (c == ']' and stk[-1] != '[') \
                        or (c == '}' and stk[-1] != '{'):
                return False
            else:
                stk.pop()
        
        return not stk
            
    # O(N)
    # Faster than the first
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in "([{":
                stk.append(c)
            else:
                if not stk:
                    return False
                h = stk.pop()
                if (c == ')' and h != '(') or (c == ']' and h != '[') or (c == '}' and h != '{'):
                    return False
                    
        return not stk
    
    # O(N)
    # Better if
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in "([{":
                stk.append(c)
            else:
                if not stk:
                    return False
                h = stk.pop()
                if [h, c] not in [['(', ')'], ['[', ']'], ['{', '}']]:
                    return False
                    
        return not stk