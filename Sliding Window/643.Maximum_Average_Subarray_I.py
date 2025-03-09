# O(N)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        maxi = summ / k

        for window in range(len(nums) - k):
            summ += nums[window + k] - nums[window]
            maxi = max(maxi, summ / k)
            
        return maxi
