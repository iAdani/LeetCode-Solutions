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
            