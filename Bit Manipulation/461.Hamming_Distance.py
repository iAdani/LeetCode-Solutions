class Solution:
    # O(N)
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        while x or y:
            count += (x & 1) ^ (y & 1)
            x >>= 1
            y >>= 1

        return count
    
    # O(k)
    # where k is the highest bit after xor
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        x = x ^ y
        while x:
            count += x & 1
            x >>= 1

        return count