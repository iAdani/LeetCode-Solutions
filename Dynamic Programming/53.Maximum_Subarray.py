class Solution:
    # O(N)
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > 0:
                if curr_sum > 0:
                    curr_sum += nums[i]
                else:
                    curr_sum = nums[i]
            else:
                if curr_sum > 0:
                    curr_sum += nums[i]
                else:
                    curr_sum = max(curr_sum, nums[i])
            
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
    

    # O(N)
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
            curr_sum = max(curr_sum, 0)
            
        return max_sum


    # O(N)
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
