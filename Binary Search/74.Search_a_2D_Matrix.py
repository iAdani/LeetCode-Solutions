class Solution:
    # O(log(n * m))
    # Since log(a) + log(b) = log(ab)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        b, t = n - 1, 0
        while b > t:
            middle = b + ((t - b) // 2)
            if matrix[middle][-1] == target:
                return True
            if matrix[middle][-1] > target:
                b = middle
            else:
                t = middle + 1
        
        r, l = m - 1, 0
        while r >= l:
            middle = r + ((l - r) // 2)
            if matrix[b][middle] == target:
                return True
            if matrix[b][middle] > target:
                r = middle - 1
            else:
                l = middle + 1
        
        return False
    
    # O(log(n * m))
    # Another version
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        r, l = m * n - 1, 0
        while r >= l:
            mid = r + ((l - r) // 2)
            i, j = mid // m, mid % m
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False
