import heapq

class Solution:
    # O(N * log(k))
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            d = (point[0] ** 2) + (point[1] ** 2)
            heapq.heappush(heap, (-d, point))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [item[1] for item in heap]