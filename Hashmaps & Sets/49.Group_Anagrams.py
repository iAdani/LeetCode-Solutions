# O(n * m)
class Solution:
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
    