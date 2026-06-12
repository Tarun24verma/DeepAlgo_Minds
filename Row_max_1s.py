class Solution:
    def rowWithMax1s(self, arr):
        b=[]
        c=0
        m=0
        for i in range(len(arr)):
            if arr[i].count(1)>c:
                c=arr[i].count(1)
                m=i
        if c==0:
            return -1
        else:
            return m