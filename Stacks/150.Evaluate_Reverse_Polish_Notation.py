# O(N)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token not in '+-*/':
                stk.append(int(token))
            else:
                last = stk.pop()
                match token:
                    case '+':
                        stk[-1] += last
                    case '-':                
                        stk[-1] -= last
                    case '*':
                        stk[-1] *= last
                    case '/':
                        res = stk[-1] / last
                        if res > 0:
                            stk[-1] = math.floor(res)
                        else:
                            stk[-1] = math.ceil(res)
            
        return stk[0]
        