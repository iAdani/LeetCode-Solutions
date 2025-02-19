# O(N)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        lowest = prices[0]

        for price in prices[1:]:
            if price - lowest > maximum:
                maximum = price - lowest
            lowest = min(lowest, price)

        return maximum