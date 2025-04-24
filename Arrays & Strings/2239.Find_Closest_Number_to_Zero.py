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
    
    # O(N)
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = (100001, 0)
        for num in nums:
            if abs(num) < closest[0]:
                closest = (abs(num), num)
        
        return closest[0] if closest[1] < 0 and closest[0] in nums else closest[1]
