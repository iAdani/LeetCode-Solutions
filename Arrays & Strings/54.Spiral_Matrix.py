# O(N*M)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        mxn = m * n
        res = []
        i, j = 0, 0
        UP_WALL, RIGHT_WALL, DOWN_WALL, LEFT_WALL = 0, n, m, -1
        direction = 0

        while len(res) < mxn:
            match direction:
                case 0:
                    while j < RIGHT_WALL:
                        res.append(matrix[i][j])
                        j += 1
                    
                    i, j = i + 1, j - 1
                    RIGHT_WALL -= 1

                case 1:
                    while i < DOWN_WALL:
                        res.append(matrix[i][j])
                        i += 1

                    i, j = i - 1, j - 1
                    DOWN_WALL -= 1
                
                case 2:
                    while j > LEFT_WALL:
                        res.append(matrix[i][j])
                        j -= 1

                    i, j = i - 1, j + 1
                    LEFT_WALL += 1
                
                case 3:
                    while i > UP_WALL:
                        res.append(matrix[i][j])
                        i -= 1

                    i, j = i + 1, j + 1
                    UP_WALL += 1
            
            direction = (direction + 1) % 4

        return res
           