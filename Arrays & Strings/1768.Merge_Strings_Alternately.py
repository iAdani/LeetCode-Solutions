import time

class Solution:
    # O(N)
    def mergeAlternately1(self, word1: str, word2: str) -> str:
        merged = ''
        idx = 0
        while idx < min(len(word1), len(word2)):
            merged += word1[idx] + word2[idx]
            idx += 1
        
        if idx < len(word1):
            merged += word1[idx:]
        if idx < len(word2):
            merged += word2[idx:]
        
        return merged
    
    # O(N)
    def mergeAlternately2(self, word1: str, word2: str) -> str:
        res = ''
        n, m = len(word1), len(word2)
        i = 0
        while i < min(n, m):
            res += word1[i]
            res += word2[i]
            i += 1
        
        while i < n:
            res += word1[i]
            i += 1
        while i < m:
            res += word2[i]
            i += 1
        
        return res
    
    # O(N)
    def mergeAlternately3(self, word1: str, word2: str) -> str:
        merged = ''
        i = 0
        while i < min(len(word1), len(word2)):
            merged += word1[i] + word2[i]
            i += 1
        
        merged += word1[i:] + word2[i:]
        return merged

    # O(N)
    # Practically A LOT faster than String +=
    def mergeAlternately4(self, word1: str, word2: str) -> str:
        result = []
        i, lenn = 0, min(len(word1), len(word2))
        while i < lenn:
            result.append(word1[i])
            result.append(word2[i])
            i += 1

        result.append(word1[i:])
        result.append(word2[i:])
        return ''.join(result)

    # O(N)
    # Even faster
    def mergeAlternately5(self, word1: str, word2: str) -> str:
        sol = []
        for c1, c2 in zip(word1, word2):
            sol.extend([c1, c2])
        
        n = len(sol)
        sol.extend(list([word1[n//2:], word2[n//2:]]))
        return "".join(sol)
    

word1 = 'A' * 999999
word2 = 'B' * 990009

start_time = time.time()
res = Solution().mergeAlternately4(word1, word2)
print(f"--- {(time.time() - start_time)} seconds ---")

start_time = time.time()
res = Solution().mergeAlternately5(word1, word2)
print(f"--- {(time.time() - start_time)} seconds ---")

# Result:
# String += 
# --- 165.69983291625977 seconds ---
# List + join
# --- 0.118988037109375 seconds ---