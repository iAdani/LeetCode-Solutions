# O(N)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(t), len(s)
        t_idx = s_idx = 0

        while t_idx < n and s_idx < m:
            if t[t_idx] == s[s_idx]:
                s_idx += 1
            t_idx += 1
        
        if s_idx == m:
            return True
        
        return False