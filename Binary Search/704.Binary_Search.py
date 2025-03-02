class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r, l = len(nums) - 1, 0
        while r >= l:
            m = r + ((l - r) // 2)
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1
        