class Solution:
    # Time: O(n * m), Space: O(n * m)
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        islands = 0

        def clearIsland(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                grid[i][j] = '0'
                clearIsland(i, j + 1)
                clearIsland(i + 1, j)
                clearIsland(i, j - 1)
                clearIsland(i - 1, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    clearIsland(i, j)
                    islands += 1
        
        return islands

