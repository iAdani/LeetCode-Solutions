# O(N)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        return False if len(nums) == len (nums_set) else True