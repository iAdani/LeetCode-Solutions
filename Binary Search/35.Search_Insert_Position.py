# O(log(N))
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while r >= l:
            m = r - ((r - l) // 2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return m if nums[m] > target else m + 1
        