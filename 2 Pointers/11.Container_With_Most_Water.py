class Solution:
    # O(N)
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        max_container = 0

        while start < end:
            container = min(height[start], height[end]) * (end - start)
            max_container = max(max_container, container)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        
        return max_container

