class Solution(object):
    # Time: O(N), Space: O(N)
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        sum_array = [nums[0]]
        for num in nums[1:]:
            sum_array.append(sum_array[-1] + num)
        
        return sum_array
    
    # Time: O(N), Space: O(1)
    # In-place modification of the input array
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        return nums