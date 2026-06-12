class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        k=0
        for j in range(len(matrix)):
            if matrix[j][0]<=target:
                k=j
        if target in matrix[k]:
            return True
        else:
            return False