class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        matrix = [element for row in grid for element in row]
        matrix.sort()
        t = matrix[len(matrix) // 2]
        op = 0
        for v in matrix:
            if abs(v - t) % x != 0:
                return -1
            op += abs(v - t) // x
        return op