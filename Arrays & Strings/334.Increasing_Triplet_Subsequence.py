class Solution:
    # Time: O(N), Space: O(1)
    # The idea is going left to right, and when a number is greater tham i and j, it's a triplet.
    # If j got a value, even if i is to the left, it still means that there is a number to the
    # right of j that is smaller than it. So if we find a number bigger than j, it's a triplet.
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = j = float('inf')
        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True
        
        return False
        

    # Time: O(N), Space: O(N)
    # Practically not very efficient, but it's a great idea (not mine) that i wish to keep.
    # The idea is to create two arrays, one for the minimum value to the left of each element
    # and one for the maximum value to the right of each element. 
    # Then checking if there is a number in the middle that satisfies the condition.
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        min_arr = [0] * n
        min_arr[0] = nums[0]

        max_arr = [0] * n
        max_arr[-1] = nums[-1]

        for i in range(1, n):
            if min_arr[i - 1] < nums[i]:
                min_arr[i] = min_arr[i - 1]
            else:
                min_arr[i] = nums[i]

        for i in range(n - 2, -1, -1):
            if max_arr[i + 1] > nums[i]:
                max_arr[i] = max_arr[i + 1]
            else:
                max_arr[i] = nums[i]
        
        for i in range(1, n - 1):
            if min_arr[i] < nums[i] < max_arr[i]:
                return True
        
        return False

    # Time: O(N), Space: O(N)
    # Same idea as the previous one, but using only one array. Very slow.
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        max_arr = [0] * n
        max_arr[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            max_arr[i] = max(max_arr[i + 1], nums[i + 1])
        
        min_left = nums[0]
        for i in range(1, n - 1):
            if min_left < nums[i] < max_arr[i]:
                return True
            min_left = min(min_left, nums[i])
        
        return False
