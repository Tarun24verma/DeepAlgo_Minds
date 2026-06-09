class Solution:
    def countBits(self, n: int) -> list[int]:
        def binaryn(n):
            if n==0:
                return ""
            return binaryn(n//2)+str(n%2)
        arr=[]
        for i in range(n+1):
            c=0
            t=binaryn(i)
            print(t)
            for j in t:
                if j=='1':
                    c+=1
            arr.append(c)
        return arr

            