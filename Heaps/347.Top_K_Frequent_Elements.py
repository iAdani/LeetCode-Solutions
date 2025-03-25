import heapq
from collections import Counter

class Solution:
    # O(N * log(k))
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pairs, heap = {}, []
        for num in nums:
            count = pairs.get(num, 0)
            pairs[num] = count + 1
        
        for key, val in pairs.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [key for (val, key) in heap]


    # O(N)  
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter, buckets = Counter(nums), [[] for _ in range(n + 1)] 
        for num, freq in counter.items():
            buckets[freq].append(num)
        
        res = []
        while n > -1:
            res.extend(buckets[n])
            n -= 1

            if len(res) == k:
                break
        
        return res
        
