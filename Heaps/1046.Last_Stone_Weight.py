import heapq
class Solution:
    # O(N*log(N))
    # heapify: O(N), pop: O(log(N)), push: O(log(N))
    # While loops makes stones length shorter by 1 each time - O(N)
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first != second:
                heapq.heappush(stones, first - second)
        
        return 0 if not stones else -stones[0]
