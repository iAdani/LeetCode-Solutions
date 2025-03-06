class Solution:
    # Time: O(N), Space: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        count = 1
        for num in nums[1:]:
            if num == major:
                count += 1
            elif count > 0:
                count -= 1
            else:
                major = num
                count = 1
        
        return major
    

    # Time: O(N), Space: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        major = count = 0
        for num in nums:
            if count == 0:
                major = num
            
            if major == num:
                count += 1
            else:
                count -= 1
        
        return major