class Solution:
    def sortedMatrix(self, mat):
        temp = []
        n = len(mat)
        for row in mat:
            temp.extend(row)
        temp.sort()
        return [temp[i:i + n] for i in range(0, len(temp), n)]