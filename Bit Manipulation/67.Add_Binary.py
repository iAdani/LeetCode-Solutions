class Solution:
    # O(n)
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)
        a += b
        return bin(a)[2:]
    
    # O(n + m)
    # n,m are the length of bits in a,b
    # This is a version where + is not allowed
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)
        
        while b:
            without_carry = a ^ b
            b = (a & b) << 1
            a = without_carry
        
        return bin(a)[2:]
        
