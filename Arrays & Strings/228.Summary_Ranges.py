# O(N)
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
            
        lst = []
        current = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] - 1 != current[-1]:
                if len(current) > 1:
                    lst.append(f"{current[0]}->{current[-1]}")
                else:
                    lst.append(f"{current[0]}")
                
                current.clear()
            
            current.append(nums[i])
        
        if len(current) > 1:
            lst.append(f"{current[0]}->{current[-1]}")
        else:
            lst.append(f"{current[0]}")
        
        return lst