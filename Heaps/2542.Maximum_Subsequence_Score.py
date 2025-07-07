import heapq

class Solution:
    # O(n * log(n))
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(nums1[i], nums2[i]) for i in range(len(nums1))]
        pairs.sort(key = lambda x: x[1], reverse = True)

        max_score = summ = 0
        heap = []
        for num1, num2 in pairs:
            heapq.heappush(heap, num1)
            summ += num1
            if len(heap) > k:
                summ -= heapq.heappop(heap)
            
            if len(heap) == k:
                max_score = max(max_score, summ * num2)
        
        return max_score
