class Solution:
    # Time: O(N), Space: O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]
        for i in range(1, n):
            prefix.append(prefix[-1] * nums[i - 1])
        
        suffix = [1] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        for i in range(n):
            prefix[i] *= suffix[i]
        return prefix
    
    # Time: O(N), Space: O(1)
    # Space is O(1) because the returned array doesn't count
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]
        for i in range(1, n):
            prefix.append(prefix[-1] * nums[i - 1])
        
        for i in range(n - 2, -1, -1):
            nums[i] *= nums[i + 1]

        for i in range(n - 1):
            prefix[i] *= nums[i + 1]
        return prefix
