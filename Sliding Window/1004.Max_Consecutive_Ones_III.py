class Solution:
    # O(N)
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroes = 0
        maxi = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes += 1
            
            while zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1
            
            maxi = max(maxi, r - l + 1)
        
        return maxi
                