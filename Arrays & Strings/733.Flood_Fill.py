class Solution:
    # O(n * m)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])

        def flood(sr, sc, color, n, m):
            original_color = image[sr][sc]
            image[sr][sc] = color
            if original_color == color:
                return

            if sr < n - 1 and image[sr + 1][sc] == original_color:
                flood(sr + 1, sc, color, n, m)
            if sr and image[sr - 1][sc] == original_color:
                flood(sr - 1, sc, color, n, m)
            if sc < m - 1 and image[sr][sc + 1] == original_color:
                flood(sr, sc + 1, color, n, m)
            if sc and image[sr][sc - 1] == original_color:
                flood(sr, sc - 1, color, n, m)

        flood(sr, sc, color, n, m)
        return image
        