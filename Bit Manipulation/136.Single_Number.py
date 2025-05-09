class Solution:
    # Time: O(N), Space: O(1)
    def singleNumber(self, nums: List[int]) -> int:
        xor = nums[0]
        for num in nums[1:]:
            xor ^= num
        
        return xor