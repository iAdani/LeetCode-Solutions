class Solution:
    # O(N^2)
    def tupleSameProduct(self, nums: List[int]) -> int:
        dictt = {}
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = nums[i], nums[j]
                count = dictt.get(a * b, 0)
                dictt[a * b] = count + 1
        
        count = 0
        for val in dictt.values():
            if val >= 2:
                count += (math.factorial(val) // math.factorial(val - 2)) * 4
        return count
