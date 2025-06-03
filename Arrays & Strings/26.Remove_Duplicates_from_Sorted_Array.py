class Solution:
    # O(N)
    def removeDuplicates(self, nums: List[int]) -> int:
        scanner = insert = 0
        while scanner < len(nums):
            char = nums[scanner]
            while scanner < len(nums) and nums[scanner] == char:
                scanner += 1
                
            nums[insert] = char
            insert += 1
        
        return insert
    
    
    # O(N)
    def removeDuplicates(self, nums: List[int]) -> int:
        insert = 0
        for i in range(len(nums)):
            if nums[i] != nums[insert]:
                insert += 1
                nums[insert] = nums[i]
        
        return insert + 1