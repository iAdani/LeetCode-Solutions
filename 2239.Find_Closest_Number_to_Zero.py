class Solution:
    # O(N)
    def findClosestNumber(self, nums: List[int]) -> int:
        abs_nums = [abs(x) for x in nums]
        res = min(abs_nums)
        if res in nums:
            return res
        return -res
    
    # O(N) 
    def findClosestNumber(self, nums: List[int]) -> int:
        res = 100001
        negative = False

        for num in nums:
            if abs(num) < res:
                res = abs(num)
                negative = num < 0
            
            if abs(num) == res and negative:
                res = abs(num)
                negative = num < 0

        return -res if negative else res
