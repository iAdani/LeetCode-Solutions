class Solution:
    # O(N)
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        removed = 0
        last_end = intervals[0][0]

        for interval in intervals:
            if interval[0] < last_end:
                removed += 1
            else:
                last_end = interval[1]
        
        return removed
