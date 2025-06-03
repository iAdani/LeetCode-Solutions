class Solution:
    # Time: O(n * m), Space: O(n * m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = {}
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1

            key = tuple(freq)
            if key not in dictt:
                dictt[key] = [s]
            else:
                dictt[key].append(s)
        
        return list(dictt.values())
    

    # Time: O(n * m), Space: O(n * m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            
            anagrams[tuple(freq)].append(word)
            
        return list(anagrams.values())
    