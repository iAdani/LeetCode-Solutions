class Solution:
    # Time: O(N), Space: O(1)
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        curr = 1
        for _ in range(n):
            res.append(curr)

            # If possible, go to next "depth" by adding a zero
            if curr * 10 <= n:
                curr *= 10
            else:
                # If added all 9 digits in that depth or got to n - backtrack
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10     # remove last digit
                curr += 1           # move to the next lex. number
        
        return res