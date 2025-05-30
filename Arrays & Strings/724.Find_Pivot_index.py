class Solution:
    # Time: O(N), Space: O(N)
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sum_right = 0
        sum_left = [0] * n
        for i in range(n - 2, -1, -1):
            sum_left[i] = nums[i + 1] + sum_left[i + 1]
        
        for i in range(n):
            if sum_right == sum_left[i]:
                return i
            sum_right += nums[i]

        return -1
    

    # Time: O(N), Space: O(1)
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sum_right, sum_left = 0, sum(nums)
        
        for i in range(n):
            sum_left -= nums[i]
            if sum_right == sum_left:
                return i
            sum_right += nums[i]

        return -1