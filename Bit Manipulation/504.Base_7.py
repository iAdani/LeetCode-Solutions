class Solution:
    # O(log(N))
    def convertToBase7(self, num: int) -> str:
        if not num:
            return '0'

        sign = 0
        if num < 0:
            sign = 1
            num *= -1

        s = ''
        while num:
            s += str(num % 7)
            num //= 7
        
        if sign:
            s += '-'
            
        return s[::-1]