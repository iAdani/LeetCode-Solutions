class Solution:
    # O(N^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        n = len(nums)
        i = 0
        while i < len(nums) and nums[i] < 1:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            low, high = i + 1, n - 1
            first = nums[i]
            while high > low:
                summ = first + nums[low] + nums[high]
                if summ > 0:
                    high -= 1
                elif summ < 0:
                    low += 1
                else:
                    triplets.append([first, nums[low], nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low += 1
                    high -= 1
            
            i += 1
        
        return triplets
                        
