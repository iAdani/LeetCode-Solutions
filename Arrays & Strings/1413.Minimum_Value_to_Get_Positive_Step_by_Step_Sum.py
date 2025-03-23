class Solution:
    # O(N)
    def minStartValue(self, nums: List[int]) -> int:
        minn = 9999999
        summ = 0
        for num in nums:
            summ += num
            minn = min(minn, summ)
        
        return 1 if minn > 0 else -minn + 1
