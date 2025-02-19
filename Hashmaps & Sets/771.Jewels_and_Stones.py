class Solution:
    # Time: O(n * m), Space: O(1)
    # 'm' is jewels len and 'n' is stones len.
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        
        return count
    
    
    # Time: O(n + m), Space: O(m)
    # 'm' is jewels len and 'n' is stones len.
    # It takes m time to build the set but O(1) to search in it.
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        
        return count