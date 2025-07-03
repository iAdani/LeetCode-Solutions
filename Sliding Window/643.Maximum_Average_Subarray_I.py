class Solution:
    # O(N)
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        maxi = summ / k

        for window in range(len(nums) - k):
            summ += nums[window + k] - nums[window]
            maxi = max(maxi, summ / k)
            
        return maxi


    # O(N)
    # Improvement, only one division 
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = maxi = sum(nums[:k])
        for window in range(len(nums) - k):
            summ += nums[window + k] - nums[window]
            maxi = max(maxi, summ)
            
        return maxi / k
        