# Time: O(N), Space: O(1)
# One pass over the input and constant space
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if nums[white] == 2:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
            else:
                if nums[white] == 0:
                    nums[red], nums[white] = nums[white], nums[red]
                    red += 1            
                white += 1        
        return nums
 