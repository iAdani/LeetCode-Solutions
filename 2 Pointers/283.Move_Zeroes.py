class Solution:
    # Time: O(N), Space: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
     
    
    # Time: O(N), Space: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        zero_count = 0
        for i, num in enumerate(nums):
            if num == 0:
                zero_count += 1
            else:
                nums[i - zero_count] = num
        
        for i in range(zero_count, 0, -1):
            nums[-i] = 0

    
    # Time: O(N), Space: O(1)
    # i != pos saves time even though both are O(N)
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != pos:
                    nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
            