class Solution:
    # O(Nlog(N))
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [x * x for x in nums]
        return sorted(squares)
    
    # Time: O(N), Space: O(N)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = [x ** 2 for x in nums]

        pos1, pos2 = 0, n - 1
        res = []
        while pos1 <= pos2:
            if nums[pos1] > nums[pos2]:
                res.append(nums[pos1])
                pos1 += 1
            else:
                res.append(nums[pos2])
                pos2 -= 1
                
        return res[::-1]
