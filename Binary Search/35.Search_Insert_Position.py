# O(log(N))
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        r, l = len(nums) - 1, 0

        while r >= l:
            m = r + ((l - r) // 2)
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        

        return m if nums[m] > target else m + 1
        