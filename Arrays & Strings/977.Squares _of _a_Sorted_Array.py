# O(Nlog(N))
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [x * x for x in nums]
        return sorted(squares)