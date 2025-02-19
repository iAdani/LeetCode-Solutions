# O(Nlog(N))
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        start, end = 0, n -1
        original_nums = nums.copy()
        nums = sorted(nums)

        while start < end:
            while target - nums[start] < nums[end]:
                end -= 1
            
            if nums[start] + nums[end] == target:
                if nums[start] != nums[end]:
                    return [original_nums.index(nums[start]), original_nums.index(nums[end])]
                idx = original_nums.index(nums[start])
                return [idx, original_nums.index(nums[end], idx + 1)]
            
            start += 1
        
        return [-1, -1]
        