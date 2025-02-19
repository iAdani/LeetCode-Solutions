class Solution:
    def romanToInt(self, s: str) -> int:
        res = idx = 0
        n = len(s)
        while idx < n:
            match s[idx]:
                case 'M':
                    res += 1000      
                case 'D':
                    res += 500
                case 'L':
                    res += 50
                case 'V':
                    res += 5
                case 'C':
                    res += 100
                    if idx < n - 1:
                        if s[idx + 1] == 'D' or s[idx + 1] == 'M':
                            if s[idx + 1] == 'M':
                                res += 500
                            res += 300
                            idx += 1
                case 'X':
                    res += 10
                    if idx < n - 1:
                        if s[idx + 1] == 'L' or s[idx + 1] == 'C':
                            if s[idx + 1] == 'C':
                                res += 50
                            res += 30
                            idx += 1
                case 'I':
                    res += 1
                    if idx < n - 1:
                        if s[idx + 1] == 'X' or s[idx + 1] == 'V':
                            if s[idx + 1] == 'X':
                                res += 5
                            res += 3
                            idx += 1
                
            idx += 1

        return res
