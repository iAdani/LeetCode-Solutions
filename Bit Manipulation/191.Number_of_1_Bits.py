class Solution:
    # O(k)
    # k is ht enumber of 1's in the binary representation.
    # At the worst case, k equals the length of the binary representation.
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n &= n - 1
        
        return count