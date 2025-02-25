class Solution:
    # O(Nlog(N))
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        start, end = 0, n -1
        original_nums = nums.copy()
        nums = sorted(nums)

        while start < end:
            while target - nums[start] < nums[end]:
                end -= 1
            
            if nums[start] + nums[end] == target:
                if nums[start] != nums[end]:
                    return [original_nums.index(nums[start]), original_nums.index(nums[end])]
                idx = original_nums.index(nums[start])
                return [idx, original_nums.index(nums[end], idx + 1)]
            
            start += 1
        
        return [-1, -1]
    
    # O(N)
    # Using dictionary (HashMap) in() is O(1) and we pass over nums
    # only twice, therefore O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        n = len(nums)
        for i in range(n):
            nums_dict[nums[i]] = i
        
        for i in range(n):
            x = target - nums[i]
            if x in nums_dict and nums_dict[x] != i:
                return [i, nums_dict[x]]   
        