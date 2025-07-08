class Solution:
    # O(N)
    def tribonacci(self, n: int) -> int:
        nums = [0, 1, 1]
        for i in range(3, n + 1):
            nums.append(nums[i - 3] + nums[i - 2] + nums[i - 1])
        
        return nums[n]
