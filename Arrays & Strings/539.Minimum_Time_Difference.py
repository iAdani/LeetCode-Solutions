class Solution:
    # O(N)
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        for i in range(n):
            timePoints[i] = int(timePoints[i][:2]) * 60 + int(timePoints[i][3:])
        timePoints.sort()
        
        timePoints.append(timePoints[0] + 1440)
        minn = 1441
        for i in range(1, n + 1):
            minn = min(minn, timePoints[i] - timePoints[i - 1])

        return minn
    