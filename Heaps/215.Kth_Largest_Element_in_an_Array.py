import heapq

class Solution:
    # O(N * logn(N))
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, -num)
            
        
        for _ in range(k - 1):
            heapq.heappop(heap)
        
        return -heapq.heappop(heap)
    

    # O(N * log(k))
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
            
        return heap[0]
    
    