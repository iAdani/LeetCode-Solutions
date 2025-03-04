# O(log(N))
class Solution:
    def findMin(self, nums: List[int]) -> int:
        r, l = len(nums) - 1 , 0
        while nums[l] > nums[r]:
            m = r + ((l - r) // 2)
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        return nums[l]
    