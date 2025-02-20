# O(N)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)

        for idx in range (min_len):
            for s in strs:
                if s[idx] != strs[0][idx]:
                    return s[:idx]

        return [s for s in strs if len(s) == min_len][0]