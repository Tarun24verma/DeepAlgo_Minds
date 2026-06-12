class Solution:
    def median(self, mat):
        arr = []
        for i in range(len(mat)):
            arr.extend(mat[i])
        arr.sort()
        n = len(arr)
        if n % 2 == 0:
            median = (arr[n // 2 - 1] + arr[n // 2]) // 2
        else:
            median = arr[n // 2]
        return median
