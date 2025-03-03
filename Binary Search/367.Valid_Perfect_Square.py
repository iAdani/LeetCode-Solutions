# O(log(N))
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r, l = num, 1
        while r >= l:
            m = r + ((l - r) // 2)
            sq = m ** 2
            if sq == num:
                return True
            if sq > num:
                r = m - 1
            else:
                l = m + 1
        
        return False