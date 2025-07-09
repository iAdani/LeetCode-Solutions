class Solution:
    # O(N)
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        max_candies = max(candies)
        result = [False] * n
        for i in range(n):
            if candies[i] + extraCandies >= max_candies:
                result[i] = True
        
        return result


    # O(N)
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        limit = max(candies) - extraCandies
        return [candy >= limit for candy in candies]