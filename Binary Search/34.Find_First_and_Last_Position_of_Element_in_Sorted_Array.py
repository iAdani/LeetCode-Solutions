class Solution:
    # O(log(N))
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        def first_search(nums, target):
            l, r = 0, len(nums) - 1
            while r >= l:
                m = r - ((r - l) // 2)
                if nums[m] >= target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m
                
            return l
        

        def last_search(nums, target):
            l, r = 0, len(nums) - 1
            while r > l:
                m = r - ((r - l) // 2)
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    l = m

            return r

        
        first = first_search(nums, target)
        last = last_search(nums,target)
        if first == len(nums) or nums[first] != target:
            first = -1
        if last == len(nums) or nums[last] != target:
            last = -1

        return [first, last]


    # O(log(N))
    # More compact solution
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(is_left):
            l, r = 0, len(nums) - 1
            idx = -1
            while r >= l:
                m = r - ((r - l) // 2)
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    idx = m
                    if(is_left):
                        r = m - 1
                    else:
                        l = m + 1
                
            return idx
        
        return [binary_search(True), binary_search(False)]