class Solution:
    # O(N)
    # Using dict
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        l = longest = 0
        for r in range(len(s)):
            count = seen.get(s[r], 0)
            seen[s[r]] = count + 1

            while (r - l + 1) - max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest
    
    # O(N)
    # Using list
    def characterReplacement(self, s: str, k: int) -> int:
        seen = [0] * 26
        l = longest = 0
        for r in range(len(s)):
            seen[ord(s[r]) - ord('A')] += 1

            while (r - l + 1) - max(seen) > k:
                seen[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest