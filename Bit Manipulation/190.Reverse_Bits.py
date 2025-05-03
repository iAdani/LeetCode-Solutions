class Solution:
    # O(log(N))
    # actually O(32) = O(1) but that O(log(N))
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            bit = n & 1
            res = (res << 1) | bit
            n >>= 1
        return res

    # O(log(N))
    def reverseBits(self, n: int) -> int:
        res = 0
        power = 31
        while n:
            res += (n & 1) << power
            n >>= 1
            power -= 1
        
        return res

