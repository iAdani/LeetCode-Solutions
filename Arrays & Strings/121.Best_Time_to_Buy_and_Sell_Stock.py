class Solution:
    # O(N)
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        lowest = prices[0]

        for price in prices[1:]:
            if price - lowest > maximum:
                maximum = price - lowest
            lowest = min(lowest, price)

        return maximum
    
    # O(N)
    # Just nicer
    def maxProfit(self, prices: List[int]) -> int:
        min_seen, max_profit = prices[0], 0
        for price in prices:
            max_profit = max(max_profit, price - min_seen)
            min_seen = min(min_seen, price)
        return max_profit