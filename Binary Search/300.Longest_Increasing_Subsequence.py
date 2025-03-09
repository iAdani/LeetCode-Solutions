class Solution(object):
    # O(log(N))
    def insert_search(self, nums, x):
        r, l = len(nums) - 1, 0
        m = 0
        while r >= l:
            m = r - ((r - l) // 2)
            if nums[m] > x:
                r = m - 1
            elif nums[m] < x:
                l = m + 1
            else:
                return m
        
        return m if nums[m] > x else m + 1
                

    # O(N*log(N))
    def lengthOfLIS(self, nums):
        lst = [nums[0]]
        for num in nums[1:]:
            pos = self.insert_search(lst, num)
            if pos == len(lst):
                lst.append(num)
            else:
                lst[pos] = num
        
        return len(lst)

