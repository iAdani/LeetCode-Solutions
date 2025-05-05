class Solution:
    # O(N)
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        return False if len(nums) == len (nums_set) else True
    
    # O(N)
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(nums) == len(set(nums)) else True